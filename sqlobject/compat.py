import sys
import types

# Credit to six authors: http://pypi.python.org/pypi/six
# License: MIT


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.

    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})

# Compatability definitions (inspired by six)
if sys.version_info[0] < 3:
    string_type = basestring
    unicode_type = unicode
    class_types = (type, types.ClassType)
    buffer_type = buffer
else:
    string_type = str
    unicode_type = str
    class_types = (type, )
    buffer_type = memoryview
