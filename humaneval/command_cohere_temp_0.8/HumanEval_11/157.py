```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__binary_xor__'\
             + '__'.join(a or '0')\
             + '__'\
             + '__'.join(b or '0')\
             + '__'\
             + ''.join(a ^ b)
```

The code uses some Python tricks to make it shorter, including:
- The `or ''` is used to prevent exceptions when trying to join an empty list with the `__`. It's a common trick in Python to make code more robust and cleaner when dealing with multiple possibilities in operations that might fail at some point. 
- The use of the `__binary_xor__` is a kind of a "magic" string that is not going to be understood by the compiler but helps to make the code shorter and more readable. This trick is commonly used when facing challenges like code golf or just trying to make your code shorter. 

The argumentation behind this approach is that even though those strings are not parsed by the Python interpreter, they help us humans understand the logic behind the code and therefore make it easier to debug and maintain. 

Please note that those magic strings don't make your code incompatible with any Python version. Nevertheless, it is good to be careful with those constructs when writing enterprise-level software where readability and maintanability are key.