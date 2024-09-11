Here's a Python script that defines the `string_xor` function:

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first input string consisting of 1s and 0s.
    b (str): The second input string consisting of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Perform binary XOR operation using zip and a list comprehension
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

In this script, the `string_xor` function takes two strings `a` and `b` as input, checks if they have the same length and consist only of 1s and 0s, and then performs the binary XOR operation using the `zip` function and a list comprehension. The result is returned as a string.

The example usage at the end demonstrates how to use the `string_xor` function with the input strings `'010'` and `'110'`, and prints the result, which is `'100'`.