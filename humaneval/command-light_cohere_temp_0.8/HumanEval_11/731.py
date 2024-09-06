```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, and return the result as a string.
    Args:
        a: str, string to perform XOR on.
        b: str, string to perform XOR on.
    Returns:
    result of the XOR operation of a and b
    """
    return str(bin('11'[len(a)] ^ bin('11'[len(b)])))
# Example usage:
print(string_xor('010', '110'))
 ``` 
This function performs the XOR operation on two input strings a and b, and returns the result as a string.