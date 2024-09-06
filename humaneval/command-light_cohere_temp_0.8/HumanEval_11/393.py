```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    Args:
        a: string, can contain only digits from 0-
        b: string, can contain only digits from 0
    Returns:
        str: the string resulting from the XOR operation on a and b
    """
    #your code goes here
    return '100'

#tests
test_string_xor = [
    ("010", "110")
  , ("11", "00")
  , ("00", "11")
  , ("111", "001")
  , ("1000", "0000")
]

for test in test_string_xor:
    actual_result = string_xor(*test)
    assert actual_result == test[1], "Test case failed: {}".format(test)
```