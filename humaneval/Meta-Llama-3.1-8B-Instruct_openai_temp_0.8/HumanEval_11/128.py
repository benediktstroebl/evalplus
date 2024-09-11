```markdown
### Binary XOR Operation on Strings
#### Problem Statement
Perform binary XOR operation on two input strings consisting only of 1s and 0s.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary XOR result of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current pair of characters
        # '0' XOR '0' = '0', '0' XOR '1' = '1', '1' XOR '0' = '1', '1' XOR '1' = '0'
        if (char_a == '0' and char_b == '0') or (char_a == '1' and char_b == '1'):
            result += '0'
        else:
            result += '1'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('1010', '1100'))  # Expected output: '0110'
```

#### Explanation

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input. It iterates over the characters in these strings, performs a binary XOR operation on each pair of characters, and appends the result to a new string. Finally, it returns the resulting binary string. The function is tested with two example use cases.