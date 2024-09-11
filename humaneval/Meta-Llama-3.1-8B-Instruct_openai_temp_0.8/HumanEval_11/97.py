Here's a self-contained Python script that solves the problem:

```markdown
### Binary XOR Operation on Strings

This script performs binary XOR operation on two input strings.

#### Code
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): First binary string
    b (str): Second binary string
    
    Returns:
    str: Result of XOR operation on a and b as a string
    
    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join('1' if c1!= c2 else '0' for c1, c2 in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```
#### Explanation
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input. It uses the `zip` function to pair corresponding characters from `a` and `b`. If the characters at a pair are different, it sets the result character to '1' (since XOR of 0 and 1 is 1, and XOR of 1 and 1 is 0, and XOR of 0 and 0 is 0). If the characters at a pair are the same, it sets the result character to '0'. The `join` function is used to concatenate the result characters into a single string.