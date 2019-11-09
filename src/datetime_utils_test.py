# coding:utf-8
"""
@author: weilong chen
"""
import unittest
import datetime as dt

from . import datetime_utils


class Test(unittest.TestCase):

    def test_truncate(self):
        dtime = dt.datetime(2019,11,7,13,45,36)
        dtime2 = datetime_utils.truncate(dtime, dt.datetime.hour)
        assert dtime2 == dt.datetime(2019,11,7,13)

    def test_ceil(self):
        dtime = dt.datetime(2019,11,7,13,45,36)
        dtime2 = datetime_utils.ceil(dtime, dt.datetime.hour)
        assert dtime2 == dt.datetime(2019,11,7,14)
        dtime2 = datetime_utils.ceil(dtime, dt.datetime.day)
        assert dtime2 == dt.datetime(2019,11,8)
        dtime3 = datetime_utils.ceil(dtime, dt.datetime.month)
        assert dtime3 == dt.datetime(2019,12,1)
        dtime4 = datetime_utils.ceil(dtime, dt.datetime.year)
        assert dtime4 == dt.datetime(2020,1,1)
        dtime = dt.datetime(2019,11,7,13,45)
        dtime5 = datetime_utils.ceil(dtime, dt.datetime.minute)
        assert dtime5 == dtime
        dtime = dt.datetime(2019,11,7)
        dtime6 = datetime_utils.ceil(dtime, dt.datetime.day)
        assert dtime6 == dtime