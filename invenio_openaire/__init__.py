# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OpenAIRE service integration for Invenio repositories."""

from __future__ import absolute_import, print_function

from .ext import InvenioOpenAIRE
from .version import __version__

__all__ = ('__version__', 'InvenioOpenAIRE')
