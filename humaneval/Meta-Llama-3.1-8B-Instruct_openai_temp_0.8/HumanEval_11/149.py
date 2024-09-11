### Binary String XOR
#### A Python Script to Perform Binary XOR on Two Binary Strings

```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input binary strings and return the result.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR of the input strings.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if the input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length.")

    # Initialize an empty list to store the XOR result
    xor_result = []

    # Iterate through the input strings
    for i in range(len(a)):
        # Perform binary XOR on the current bits
        xor_bit = str(int(a[i]) ^ int(b[i]))
        # Append the result to the list
        xor_result.append(xor_bit)

    # Join the result list into a string
    return ''.join(xor_result)


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: 100
```

This script defines a function `string_xor` that takes two binary strings as input, performs binary XOR on them, and returns the result as a string. The function first checks if the input strings are of equal length, then iterates through the strings, performs binary XOR on each pair of bits, and appends the result to a list. Finally, the function joins the list into a string and returns the result. The script includes example usage and a docstring with a usage example.