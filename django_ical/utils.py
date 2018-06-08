# -*- coding: utf-8 -*-
"""Utility functions to build calendar rules."""

# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# 3rd party
from dateutil.rrule import FREQNAMES
from icalendar.prop import vRecur


def build_rrule_from_recurrences_rrule(rule):
    """
    Build rrule dictionary for vRecur class from a django_recurrences rrule.

    django_recurrences is a popular implementation for recurrences in django.
    https://pypi.org/project/django-recurrence/
    this is a shortcut to interface between recurrences and icalendar.
    """
    from recurrence import serialize
    line = serialize(rule)
    if line.startswith('RRULE:'):
        line = line[6:]
    recurr = vRecur()
    return recurr.from_ical(line)


def build_rrule_from_dateutil_rrule(rule):
    """
    Build rrule dictionary for vRecur class from a dateutil rrule.

    Dateutils rrule is a popular implementation of rrule in python.
    https://pypi.org/project/python-dateutil/
    this is a shortcut to interface between dateutil and icalendar.
    """
    lines = str(rule).splitlines()
    for line in lines:
        if line.startswith('DTSTART:'):
            continue
        recurr = vRecur()
        return recurr.from_ical(line)


def build_rrule(count=None, interval=None, bysecond=None, byminute=None, byhour=None, byweekno=None,
                bymonthday=None, byyearday=None, bymonth=None, until=None, bysetpos=None, wkst=None, byday=None, freq=None):
    """
    Builds rrule dictionary for vRecur class
    :param count: int
    :param interval: int
    :param bysecond: int
    :param byminute: int
    :param byhour: int
    :param byweekno: int
    :param bymonthday: int
    :param byyearday: int
    :param bymonth: int
    :param until: datetime
    :param bysetpos: int
    :param wkst: str, two-letter weekday
    :param byday: weekday
    :param freq: str, frequency name ('WEEK', 'MONTH', etc)
    :return: dict
    """
    result = {}

    if count is not None:
        result['COUNT'] = count

    if interval is not None:
        result['INTERVAL'] = interval

    if bysecond is not None:
        result['BYSECOND'] = bysecond

    if byminute is not None:
        result['BYMINUTE'] = byminute

    if byhour is not None:
        result['BYHOUR'] = byhour

    if byweekno is not None:
        result['BYWEEKNO'] = byweekno

    if bymonthday is not None:
        result['BYMONTHDAY'] = bymonthday

    if byyearday is not None:
        result['BYYEARDAY'] = byyearday

    if bymonth is not None:
        result['BYMONTH'] = bymonth

    if until is not None:
        result['UNTIL'] = until

    if bysetpos is not None:
        result['BYSETPOS'] = bysetpos

    if wkst is not None:
        result['WKST'] = wkst

    if byday is not None:
        result['BYDAY'] = byday

    if freq is not None:
        if freq not in vRecur.frequencies:
            raise ValueError('Frequency value should be one of: %s' % vRecur.frequencies)
        result['FREQ'] = freq

    return result