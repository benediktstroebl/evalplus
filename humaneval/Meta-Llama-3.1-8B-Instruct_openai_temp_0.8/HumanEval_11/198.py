```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two binary strings.
    
    Args:
    a (str): First binary string.
    b (str): Second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if inputs are valid binary strings
    if set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'}):
        # Use zip to pair corresponding bits from both strings
        # Use a list comprehension to perform XOR operation on each pair
        # The ^ operator is used for binary XOR in Python
        return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    else:
        raise ValueError("Input strings should only contain 1s and 0s.")

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This code first checks if the input strings are valid binary strings (i.e., contain only 1s and 0s). If they are, it uses a list comprehension and the `zip` function to pair corresponding bits from both strings. The XOR operation is performed by checking if the bits are different (in which case the result is 1) or the same (in which case the result is 0). The results are then joined together to form the final string. If the input strings are not valid binary strings, a `ValueError` is raised.