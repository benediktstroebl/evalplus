```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If the input strings are not of equal length or contain characters other than 1s and 0s.
    """

    # Check if the input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length.")

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform binary XOR operation on the current characters
        # The XOR operation returns 1 if the characters are different, and 0 if they are the same
        result += str(int(a[i]) ^ int(b[i]))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Test case with strings of different lengths
try:
    print(string_xor('101', '1100'))
except ValueError as e:
    print(e)  # Output: Input strings must be of equal length.

# Test case with strings containing invalid characters
try:
    print(string_xor('1012', '1101'))
except ValueError as e:
    print(e)  # Output: Input strings must consist only of 1s and 0s.
```