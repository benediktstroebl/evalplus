```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of XOR operation as a binary string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must be binary strings")
    
    # Use the zip function to pair corresponding characters from both strings
    # Convert each pair to an integer, perform XOR, and convert back to a string
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' 
                   for x, y in zip(a, b) if x == y)
```

Alternatively, you can use the built-in `map` function and a lambda function to achieve the same result in a more concise way:

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of XOR operation as a binary string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must be binary strings")
    
    return ''.join(map(lambda x, y: '1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0', a, b))
```

This script includes input validation to ensure that both inputs are strings and that they consist only of 1s and 0s. It then performs the XOR operation on each pair of corresponding characters from the two strings.