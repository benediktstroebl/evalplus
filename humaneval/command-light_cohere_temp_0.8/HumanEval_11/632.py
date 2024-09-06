```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only 1s and 0s.
    Return the XOR operation on a and b.
    return a string(map(str.maketransition, (b, a))
    )

# Test suite for function string_xor
test_suite = [
    'string_xor("010", "110") asserting '100' == "".
    'string_xor("111", "001") asserting "".==string_xor("000", "000")
    .asserting "".==string_xor("0000", "1111")
    .asserting "".=="string_xor("1010", "1111")
    'string_xor("aa", "bb") asserting False'
]
```