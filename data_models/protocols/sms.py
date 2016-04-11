################################################################################
#
#  Copyright 2014-2016 Eric Lacombe <eric.lacombe@security-labs.org>
#
################################################################################
#
#  This file is part of fuddly.
#
#  fuddly is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  fuddly is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with fuddly. If not, see <http://www.gnu.org/licenses/>
#
################################################################################import sys

from fuzzfmk.data_model import *
from fuzzfmk.value_types import *
from fuzzfmk.data_model_helpers import *

class SMS_DataModel(DataModel):

    file_extension = 'sms'

    def absorb(self, data, idx):
        pass

    def build_data_model(self):

        smstxt_desc = \
        {'name': 'smstxt',
         'contents': [
             {'name': 'len',
              'contents': MH.LEN(vt=UINT8, after_encoding=False),
              'node_args': 'user_data'},
             {'name': 'user_data',
              'contents': GSM7bitPacking(val_list=['Hello World!'], max_sz=160)
             }
         ]
        }
        self.register(smstxt_desc)

data_model = SMS_DataModel()