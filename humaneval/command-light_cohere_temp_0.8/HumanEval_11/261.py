```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 1s and 0s and return result as a string.
    :param a string a, b: str
    :return: str
    """
    # Ensure both inputs contain only digits
    a = ''.join(char for char in a if char in '01')
    b = ''.join(char for char in b if char in '01')
    
    return str(int(a ^ b))

# Test the function
print(string_xor('010', '110'))  # expected output 100
```