# -*- coding: utf-8 -*-

import click

from click_ext.params import Date


def test_date_param(runner):
    @click.command()
    @click.option('--foo', type=Date())
    def cli(foo):
        click.echo('foo=%s' % repr(foo))

    r = runner.invoke(cli, [])
    assert not r.exception and 'foo=None' in r.output
    r = runner.invoke(cli, ['--foo=bar'])
    assert r.exception and 'not a valid date' in r.output
    r = runner.invoke(cli, ['--foo=20140102'])
    assert not r.exception and 'datetime.date(2014, 1, 2)' in r.output

    @click.command()
    @click.option('--foo', type=Date('%Y-%m-%d'))
    def cli(foo):
        click.echo('foo=%s' % repr(foo))

    r = runner.invoke(cli, ['--foo=2014-01-02'])
    assert not r.exception and 'datetime.date(2014, 1, 2)' in r.output
