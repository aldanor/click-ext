# -*- coding: utf-8 -*-

import click
import datetime


class Date(click.ParamType):
    def __init__(self, format='%Y%m%d'):
        super(Date, self).__init__()
        self.format = format
        self.name = 'date'

    def convert(self, value, param, ctx):
        try:
            return datetime.datetime.strptime(value, self.format).date()
        except ValueError:
            self.fail('%s is not a valid date' % value, param, ctx)


class File(click.Path):
    def __init__(self):
        super(File, self).__init__(exists=True, file_okay=True,
            dir_okay=False, resolve_path=True, readable=True)
        self.name = 'file'


class Folder(click.Path):
    def __init__(self):
        super(Folder, self).__init__(exists=True, file_okay=False,
            dir_okay=True, resolve_path=True, readable=True)
        self.name = 'folder'
