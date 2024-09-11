### Binary String XOR
#### Problem Description
Given two binary strings `a` and `b`, perform binary XOR operation on them and return the result as a string.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.
    
    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.
        
    Returns:
        str: The result of XOR operation on a and b.
    """
    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform binary XOR on the current characters and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```
This solution defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR operation on them, and returns the result as a string. The function first checks if both inputs are of the same length to ensure that the XOR operation can be performed correctly. It then iterates over the characters in the input strings, performs binary XOR on the current characters, and appends the result to the result string. Finally, the function returns the result string.