```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): A string consisting only of 1s and 0s.
    b (str): A string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if inputs are strings and consist only of 1s and 0s
    if not (isinstance(a, str) and isinstance(b, str)):
        raise TypeError("Both inputs must be strings.")
    if not (set(a).issubset('01') and set(b).issubset('01')):
        raise ValueError("Both inputs must consist only of 1s and 0s.")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must have the same length.")
    
    # Perform binary XOR operation
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```

In this script, we first check if the inputs are valid (i.e., they are strings and consist only of 1s and 0s). Then, we check if they have the same length. If these checks pass, we perform the binary XOR operation on the input strings using a generator expression and the built-in `zip` function. The result is returned as a string.