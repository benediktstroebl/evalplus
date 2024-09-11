### Binary String XOR Function
#### Problem Description
This script defines a function `string_xor` that performs binary XOR operation on two input strings consisting of 1s and 0s.

#### Code
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the current characters from the input strings (or None if out of range)
        a_char = a[i] if i < len(a) else None
        b_char = b[i] if i < len(b) else None

        # Perform XOR operation on the current characters
        # The XOR of two bits is 1 if the bits are different, and 0 if they are the same
        result_char = '1' if (a_char == '1' and b_char == '0') or (a_char == '0' and b_char == '1') else '0'

        # Append the result of the XOR operation to the result string
        result += result_char

    # Return the result string
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

#### Explanation
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns the result of their binary XOR operation as a string. The function iterates over the characters in the input strings, performs the XOR operation on the current characters, and appends the result to the result string. The function returns the result string after iterating over all characters. The XOR operation is performed using a simple if-else statement that checks the current characters from the input strings.