```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    >>> string_xor('010', '110')
    '100'
    """
    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Perform binary XOR on the input strings
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Outputs: '100'
```

This Python script defines a function `string_xor` that takes two strings `a` and `b` as input. It checks if the input strings are of the same length and consist only of 1s and 0s. The function then performs binary XOR on the input strings using a generator expression with `zip` and returns the result as a string.

The script also includes a docstring for the `string_xor` function with a usage example and a description of the function's behavior. Additionally, it includes two checks to ensure the input strings meet the required conditions.