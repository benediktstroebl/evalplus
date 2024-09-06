```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings and return result as a string.
    Args:
        a: string, first string to be operated.
        b: string, second string to be operated
    """
    # Perform binary XOR
    # a = list(map(int, a))
    # b = list(map(int, b))
    # return ''.join(*[x ^ y for x, y in zip(a, b)] )
    return str(''.join(x ^ y for x, y in zip(a, b)))

# Test the function with input strings consisting of only digits
print(string_xor('010', '110'))  # Expected Output: '100'
``` 
This code provides a self-contained function that performs the binary XOR operation on two input strings and returns the result as a string.