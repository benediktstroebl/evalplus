### Binary String XOR in Python
#### Script
```markdown
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Initialize empty list to store result
    result = []

    # Iterate over characters in input strings
    for x, y in zip(a, b):
        # Perform XOR operation and convert to string
        result.append(str(int(x) ^ int(y)))

    # Join result list into string and return
    return ''.join(result)

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```
#### Explanation

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string.

The function first checks if the input strings consist only of 1s and 0s. If not, it raises a `ValueError`.

Then, it initializes an empty list `result` to store the result of the XOR operation.

Next, it iterates over the characters in the input strings using the `zip` function, which pairs corresponding characters from the two strings.

For each pair of characters, it performs a binary XOR operation using the `^` operator, converts the result to a string using the `str` function, and appends it to the `result` list.

Finally, it joins the `result` list into a string using the `join` function and returns it.

The script also includes some test cases to demonstrate the function's behavior.