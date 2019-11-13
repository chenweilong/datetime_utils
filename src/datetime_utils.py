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
    # field_value = getattr(dtime,field.__name__)
    field_value = {_dt.datetime.second:1,
                   _dt.datetime.minute:1*60,
                   _dt.datetime.hour:1*60*60,
                   _dt.datetime.day:1*24*60*60}
    if field in (_dt.datetime.microsecond,_dt.datetime.second,_dt.datetime.minute,_dt.datetime.hour,_dt.datetime.day):
        return truncated_datetime + _dt.timedelta(seconds=field_value[field])
    if field == _dt.datetime.month:
        return add_months(truncated_datetime,1)
    if field == _dt.datetime.year:
        return add_years(truncated_datetime,1)
    raise Exception(f"unsupport field:{field}")


def truncate(dtime, field):
    fields = [_dt.datetime.microsecond,
              _dt.datetime.second,
              _dt.datetime.minute,
              _dt.datetime.hour,
              _dt.datetime.day,
              _dt.datetime.month,
              _dt.datetime.year]
    index = fields.index(field)
    if index == -1:
        raise Exception("field is unknown!")
    if index == 0:
        return dtime
    default_values = [0,0,0,0,1,1,1]
    fields_to_truncate = fields[0:index]
    fields_with_zero_values = {field.__name__:value for field,value in zip(fields_to_truncate,default_values)}
    return dtime.replace(**fields_with_zero_values)


def add_months(dtime,m):
    year, month= divmod(dtime.month-1+m, 12)
    return dtime.replace(year = dtime.year + year, month = month+1)


def add_years(dtime,m):
    return dtime.replace(year = dtime.year + m)


def add_days(dtime,m):
    return dtime + _dt.timedelta(days=m)


def add_hours(dtime,m):
    return dtime + _dt.timedelta(hours=m)


def add_minutes(dtime,m):
    return dtime + _dt.timedelta(minutes=m)


def add_seconds(dtime,m):
    return dtime + _dt.timedelta(seconds=m)


