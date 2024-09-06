```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    :type a: str
    :type b: str
    :rtype: str
    """
    # Convert to list of characters to perform XOR
    al = list(a)
    bl = list(b)
    al.extend(0)
    bl.extend(0)
    # Perform XOR on list of characters
    result = ''.join(c for c in al if c != bl[c])
    return result

# Test cases
test_cases = [
    ("010", "110"),
    ("abc", "123"),
    ("#", "##"),
    ("beyond", "yellow"),
    ("hello", "world"),
]

for i, (a, b) in enumerate(test_cases):
    result = string_xor(a, b)
    assert result == str(test_cases[i+1])
``` 
This Python code defines a function `string_xor` that performs the XOR operation on two input strings. The function takes two strings as arguments and returns the result as a string. The function first converts the strings to lists of characters, then it performs a character-wise XOR operation, adding the corresponding characters from both strings. Finally, it converts the result back to a string and returns it. 

It also includes several test cases to verify the correctness of the `string_xor` function. The test cases include various combinations of strings with different characters, and the function is expected to correctly perform the XOR operation and return the expected result.