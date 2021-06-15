#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2021, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import

from collections import namedtuple
from uuid import uuid4


from grolt.security._cryptography import (make_self_signed_certificate,
                                          install_certificate,
                                          install_private_key)


Auth = namedtuple("Auth", ["user", "password"])


def make_auth(value=None, default_user=None, default_password=None):
    try:
        user, _, password = str(value or "").partition(":")
    except AttributeError:
        raise ValueError("Invalid auth string {!r}".format(value))
    else:
        return Auth(user or default_user or "neo4j",
                    password or default_password or uuid4().hex)
