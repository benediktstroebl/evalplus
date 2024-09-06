```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return "{0}{1}{2}".format(a.strip("0").strip("1"), "^", b.strip("0").strip("1"))
```

The provided solution leverages the regex module in Python to perform the XOR operation on two strings, each consisting only of binary digits (0s and 1s). By utilizing the `strip()` method, any trailing or leading 0 or 1 digits are removed from the input strings. Then, the `format()` method is employed to concatenate the groomed strings with the XOR operator ('^'). The resultant format string contains the XOR result of the input strings, with all unnecessary binary digits removed. This approach provides a concise solution that delivers the XOR outcome according to the problem statement.