### String XOR Binary Operation
#### A Python Script to Perform Binary XOR on Two Binary Strings

```markdown
### Code
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): The first binary string consisting of 1s and 0s.
        b (str): The second binary string consisting of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate through both strings in parallel using zip
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on each pair of bits and add to the result
        result += str(int(char_a) ^ int(char_b))

    # If one string is longer than the other, append remaining bits from the longer string
    result += a[len(b):]
    result += b[len(a):]

    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '001'))  # Expected output: '100'
print(string_xor('1111', '0000'))  # Expected output: '1111'
```

### Explanation
The code defines a function `string_xor` that takes two binary strings as input and returns their XOR result. The function iterates through both strings in parallel using the `zip` function. For each pair of bits, it performs the XOR operation using the bitwise XOR operator (`^`) and appends the result to an empty string. If one string is longer than the other, it appends the remaining bits from the longer string. The result is returned as a string.