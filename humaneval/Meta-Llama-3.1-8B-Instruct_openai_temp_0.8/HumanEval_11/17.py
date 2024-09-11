```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Convert the strings to lists of integers for XOR operation
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]

    # Perform XOR operation on the lists
    result_list = [a_num ^ b_num for a_num, b_num in zip(a_list, b_list)]

    # Convert the result list back to a string and return
    return ''.join(map(str, result_list))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```