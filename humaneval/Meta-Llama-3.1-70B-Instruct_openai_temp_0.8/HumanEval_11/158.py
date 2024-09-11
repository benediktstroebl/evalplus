```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR on two input strings a and b.
    
    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR on a and b as a string.
    """
    # Check if the lengths of a and b are equal
    if len(a)!= len(b):
        raise ValueError("Both strings must be of equal length")

    # Check if a and b consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in a and b
    for char_a, char_b in zip(a, b):
        # Perform binary XOR and convert the result to a string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test cases
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
print(string_xor('111', '111'))  # Output: '000'
```