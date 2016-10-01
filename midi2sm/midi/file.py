#                       MIT License
# 
# Copyright (c) 2016 Ennis Massey
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from enum import Enum

"""
An object representing a Standard MIDI File
"""

open

class HeaderFormat(Enum):
    single_track = 0x0
    multi_track = 0x1
    mutli_file = 0x2

class StandardMIDIHeader:
    def __init__(self,
                 magic_number: int = 0x4D546864,
                 header_length: int = 0x6, ):
        self.magic_number = 0x4D546864  # MIDI Files always start with MThd
        self.header_length = 0x6  # Almost always 6 bytes long
        self.format = HeaderFormat.single_track  # Default value
        self.track_quantity = None  # This is not defaultable
        self.tick_division = None
        # Error Checking
        if not isinstance(self.format, HeaderFormat):
            raise TypeError("format should be a value present in HeaderFormat")