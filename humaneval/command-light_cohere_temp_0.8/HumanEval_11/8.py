```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Use list comprehension to convert both inputs to lists of integers
    num_list_a = list(map(int, a))
    num_list_b = list(map(int, b))
    return "".join(str(num[0] ^ num[1]) for num in zip(num_list_a, num_list_b))
```