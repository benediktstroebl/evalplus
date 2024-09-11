```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either of the input strings contains characters other than 1s and 0s.
    """

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain 1s and 0s.")

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    # Initialize an empty list to store the XOR result
    result = []

    # Perform XOR operation on each pair of characters from the input strings
    for char_a, char_b in zip(a, b):
        # XOR operation: (0, 0) -> 0, (0, 1) -> 1, (1, 0) -> 1, (1, 1) -> 0
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the XOR result into a string and return it
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script first checks if the input strings contain only 1s and 0s and if they are of the same length. It then performs the XOR operation on each pair of characters from the input strings and stores the result in a list. Finally, it joins the result list into a string and returns it. The XOR operation is performed using the `^` operator, which returns 1 if the two operands are different and 0 if they are the same.