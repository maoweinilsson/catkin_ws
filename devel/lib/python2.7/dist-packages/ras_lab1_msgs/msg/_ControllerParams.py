# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ras_lab1_msgs/ControllerParams.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ControllerParams(genpy.Message):
  _md5sum = "8950f824993d2867219a00186d4620f7"
  _type = "ras_lab1_msgs/ControllerParams"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# PI Control parameters
uint16 K
uint16 KI
uint16 INT_MAX
uint16 ticks

# Robot dimensions
float32 r
float32 r_l
float32 r_r
float32 B
"""
  __slots__ = ['K','KI','INT_MAX','ticks','r','r_l','r_r','B']
  _slot_types = ['uint16','uint16','uint16','uint16','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       K,KI,INT_MAX,ticks,r,r_l,r_r,B

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ControllerParams, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.K is None:
        self.K = 0
      if self.KI is None:
        self.KI = 0
      if self.INT_MAX is None:
        self.INT_MAX = 0
      if self.ticks is None:
        self.ticks = 0
      if self.r is None:
        self.r = 0.
      if self.r_l is None:
        self.r_l = 0.
      if self.r_r is None:
        self.r_r = 0.
      if self.B is None:
        self.B = 0.
    else:
      self.K = 0
      self.KI = 0
      self.INT_MAX = 0
      self.ticks = 0
      self.r = 0.
      self.r_l = 0.
      self.r_r = 0.
      self.B = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4H4f.pack(_x.K, _x.KI, _x.INT_MAX, _x.ticks, _x.r, _x.r_l, _x.r_r, _x.B))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.K, _x.KI, _x.INT_MAX, _x.ticks, _x.r, _x.r_l, _x.r_r, _x.B,) = _struct_4H4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4H4f.pack(_x.K, _x.KI, _x.INT_MAX, _x.ticks, _x.r, _x.r_l, _x.r_r, _x.B))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.K, _x.KI, _x.INT_MAX, _x.ticks, _x.r, _x.r_l, _x.r_r, _x.B,) = _struct_4H4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4H4f = struct.Struct("<4H4f")