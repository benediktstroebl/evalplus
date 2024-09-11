```markdown
### Binary String XOR Function

#### Description
This Python script implements a function to perform binary XOR operation on two strings.

#### Code

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # '1' XOR '1' = '0', '1' XOR '0' = '1', '0' XOR '1' = '1', '0' XOR '0' = '0'
        # So, we can simply concatenate the XOR result to the final string
        result += str((int(char_a) + int(char_b)) % 2)

    return result
```

#### Usage

You can use this function to perform binary XOR operation on two binary strings like this:

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '010'))  # Output: '111'
```