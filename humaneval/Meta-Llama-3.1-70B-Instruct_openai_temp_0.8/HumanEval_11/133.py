```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either input string contains characters other than 1s and 0s.
    """

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the list
        result.append(xor_result)

    # Join the list into a string and return
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Example usage:
if __name__ == "__main__":
    # Test case 1
    print(string_xor('101', '011'))  # Output: '110'

    # Test case 2
    print(string_xor('111', '111'))  # Output: '000'

    # Test case 3 (invalid input)
    try:
        print(string_xor('123', '456'))  # Raises ValueError
    except ValueError as e:
        print(e)  # Output: Input strings must consist only of 1s and 0s.
```