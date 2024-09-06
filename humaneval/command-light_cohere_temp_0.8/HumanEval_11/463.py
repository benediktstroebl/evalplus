```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two input strings a and b consisting only of ones.
    Return result as a string
    XOR operation in binary systems returns the summation of bits with value 1 in input strings.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both inputs are strings of only ones
    assert isinstance(a, str) and isinstance(b, str), "Both inputs must be strings of only ones."
    assert len(a) == len(b), "Both inputs must be the same length."

    # Use XOR logic
    result = 0
    for c in range(len(a)):
        result = (result ^ int(a[c]))
    result = (result ^ int(b[c]))
    return result
```