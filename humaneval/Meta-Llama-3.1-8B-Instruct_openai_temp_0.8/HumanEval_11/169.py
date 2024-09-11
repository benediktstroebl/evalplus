### Binary String XOR Function
#### Problem Description
Perform binary XOR operation on two binary strings and return the result as a string.

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
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the characters in a and b simultaneously
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append the result to the list
        result.append(xor_result)
    
    # If one of the strings is shorter, append 0s to the result
    max_len = max(len(a), len(b))
    result += ['0'] * (max_len - len(result))
    
    # Join the result list into a string and return
    return ''.join(result)
```

#### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
print(string_xor('111', '000'))  # Output: '111'
```