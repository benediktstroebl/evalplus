```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): First binary string.
    b (str): Second binary string.
    
    Returns:
    str: Binary XOR of a and b.
    
    Raises:
    ValueError: If a or b contain characters other than 0 or 1.
    """

    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s.")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length.")

    # Perform binary XOR
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))
    
    return result


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR as a string. It checks the inputs for validity and raises a `ValueError` if they are not valid binary strings or if they are of different lengths. The function uses a generator expression with the `zip` function to iterate over the bits of the input strings in parallel and applies the XOR operation to each pair of bits. The result is a string of '1's and '0's representing the binary XOR of the input strings.