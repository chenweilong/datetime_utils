# coding:utf-8
"""
@author: weilong chen
"""
import datetime as _dt
import time

def ceil_by_timedelta(dtime: 'datetime.datetime', delta: 'datetime.timedelta'):
    q, r = divmod(dtime - _dt.datetime.min, delta)
    return (_dt.datetime.min + (q + 1) * delta) if r else dtime


def ceil(dtime, field):
    truncated_datetime = truncate(dtime,field)
    if dtime == truncated_datetime:
        return dtime
    return truncated_datetime.replace(**{field.__name__: getattr(dtime,field.__name__) + 1})


def truncate(dtime, field):
    fields = [_dt.datetime.microsecond,
              _dt.datetime.second,
              _dt.datetime.minute,
              _dt.datetime.hour,
              _dt.datetime.day,
              _dt.datetime.month,
              _dt.datetime.year]
    default_values = [0,0,0,0,1,1,1]
    index = fields.index(field)
    fields_to_truncate = fields[0:index]
    fields_with_zero_values = {field.__name__:value for field,value in zip(fields_to_truncate,default_values)}
    return dtime.replace(**fields_with_zero_values)
