import ctypes
import numpy as np
import struct
from enum import Enum

# Maximum number of image elements
MAX_ELEMENTS = 8

# Maximum number of components per image element
MAX_COMPONENTS =  8

# Magic Cookie value
MAGIC_COOKIE = 0x802A5FD7

"""
File format definition:
magic | 4 bytes (image_offset) | 4 bytes (generic_size) | 4 bytes (industry_size) | 4 bytes (user_size) | 4 bytes (file_size) | 8 bytes (version) (string type as bytes) | 100 bytes (filename) (string type as bytes) |  12 bytes (string as bytes) |  
"""
class FileInformation :
    def __init__(self, magic_header, image_offset, generic_size,industry_size,user_size,file_size,version,filename,creation_date,creation_time):
        self.magic_header = struct.pack('>I',ctypes.c_ulong(magic_header).value)
        self.image_offset = struct.pack('>I',ctypes.c_ulong(image_offset).value)
        self.generic_size = struct.pack('>I',ctypes.c_ulong(generic_size).value)
        self.industry_size = struct.pack('>I',ctypes.c_ulong(industry_size).value)
        self.user_size = struct.pack('>I',ctypes.c_ulong(user_size).value)
        self.file_size = struct.pack('>I',ctypes.c_ulong(file_size).value)
        self.version = struct.pack('s',ctypes.c_char_p(version).value)
        self.filename = struct.pack('s',ctypes.c_char_p(filename).value)
        self.creation_date = struct.pack('s',ctypes.c_char_p(creation_date).value)
        self.creation_time = struct.pack('s',ctypes.c_char_p(creation_time).value)

#here we will need to brainstorm and see how we handle channel
#cause we need to do w*h*channel
class Interleave(Enum):
    Pixel = 0
    Line = 1
    Channel = 2
    #Pixel = [[0,0,0] for i in range(3)]
    #Line = [['0'*3,'1'*3,'2'*3] for i in range(3)]
    #figure how to implement Channel interleave (rrr..ggg..bbb..)
    #Channel = [['0'*3,'1'*3,'2'*3] for i in range(3)]
    Undefined = None


def from_internleave(x):
    if isinstance(x, Interleave):
        if x.value == 0:
            return x.Pixel
        if x.value == 1:
            return x.Line
        if x.value == 2:
            return x.Channel
        else:
            return x.Undefined

class Packing(Enum):
    #Use all bits (tight packing)
    Packed = 0
    #Byte (8-bit) boundary, left justified
    ByteLeft = 1
    # Byte (8-bit) boundary, right justified
    ByteRight = 2
    #Word (16-bit) boundary, left justified
    WordLeft = 3
    # Word (16-bit) boundary, right justified
    WordRight = 4
    #Longword (32-bit) boundary, left justified
    LongWordLeft = 5
    #Longword (32-bit) boundary, right justified
    LongWordRight = 6
    #Pack as many fields as possible per cell, only one otherwise
    PackAsManyAsPossible = 7
    Undefined = None

#needs to implement from for packing

class DataFormatInfo:
    #this needs some checking adding 
    def __init__(self,interleave,packing,data_sign,image_sense,line_padding,channel_padding,reserved):
        self.interleave = Interleave
        self.packing = Packing
        self.data_sign = bool()
        self.image_sense = bool()
        #self.line_padding =
        #self.channel_padding = 
        self.reserved = [ struct.pack('>q',ctypes.c_ulong(0).value)*20 ]

class ImageChannel():
    def __init__(self,designator,bit_depth,pixels_per_line,lines_per_element,min_data,min_quantity,max_data,max_quantity):
        pass

class Orientation(Enum):
    TopToBottomLeftToRight = 0
    TopToBottomRightToLeft = None
    BottomToTopLeftToRight = None
    BottomToTopRightToLeft = None
    LeftToRightTopToBottom = None
    RightToLeftTopToBottom = None
    LeftToRightBottomToTop = None
    RightToLeftBottomToTop = None
    Undefined = None


def fromimple(x):
    #needs more completion
    #check if typeof(x) == u8 and than do this
    if isinstance(x, Orientation):
        if x.value == 0:
            return x.TopToBottomLeftToRight
        if x.value == 1:
            return x.TopToBottomRightToLeft
        if x.value == 2:
            return x.BottomToTopLeftToRight
        else:
            return x.BottomToTopRightToLeft


class ImageInfo :
    def __init__(self,image_orientation,number_of_elements,channel,white_point,red_primary,green_primary,blue_primary,label_text):
        pass
    """
        impl Default for ImageInfo {
        fn default() -> Self {
            Self {
                image_orientation: Orientation::Undefined,
                number_of_elements: 1,
                channel: [ImageChannel::default(); MAX_ELEMENTS],
                white_point: [0.; 2],
                red_primary: [0.; 2],
                green_primary: [0.; 2],
                blue_primary: [0.; 2],
                label_text: String::new(),
            }
        }
    }
    """

class OriginationInfo:
    def __init__(self,x_offset,y_offset,source_image_file_name,source_date,source_time,input_device,input_device_model_number,input_device_serial_number,x_device_pitch,y_device_pitch,gamma):
        pass

class FilmInfo:
    def __init__(self,film_manufacturing_id_code,film_type,perfs_offset,prefix,count,format,frame_position,frame_rate,frame_id,slate_info):
        pass

class Header:
    def __init__(self,image_info,data_format_info,origination_info,film_info,user_info):
        pass
    
x = FileInformation(MAGIC_COOKIE,4,5,100,200,50,"2".encode('utf-8'),"alabala".encode('utf-8'),"11:22:2022".encode('utf-8'),"".encode('utf-8'))
print(x.creation_date)

from_internleave(Interleave.Pixel)
