# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect SDK.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.

from .base import BaseModel
from .schemas import LastRequestSchema


class LastRequest(BaseModel):
    """ Last Request object. """

    _schema = LastRequestSchema()

    type = None  # type: str
    """ (str) Type of last request. """
