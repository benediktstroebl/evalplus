```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Convert the input strings to lists of integers for easier XOR operation
    list_a = [int(bit) for bit in a]
    list_b = [int(bit) for bit in b]
    
    # Use map function to perform XOR operation on corresponding bits
    xor_result = list(map(lambda x, y: x ^ y, list_a, list_b))
    
    # Convert the list of integers back to a string
    result = ''.join(str(bit) for bit in xor_result)
    
    return result
```

This script first converts the input strings to lists of integers. It then uses the built-in `map` function to perform the XOR operation on each pair of corresponding bits from the two input strings. Finally, it converts the list of integers back to a string and returns the result.