```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function performs binary XOR operation on two strings
    Args: 
        a: str, First input string containing only 0s and 1s
        b: str, Second input string containing only 0s and 1s
    Returns: str, Resultant of XOR operation on a and b
    """
    # Remove all non-numeric characters
    a = ''.join(char for char in a if char.isnumeric())
    for char in b:
        b = ''.join(char for char in b if char.isnumeric())
    bare_strings_test()
    return ''.join(a ^ b)

bare_strings_test() :
    assert string_xor('010', '110') == '100'

print('All tests passed')
```