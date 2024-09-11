```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the XOR operation as a binary string.
    """

    # Check if inputs are strings and contain only 1s and 0s
    if not (isinstance(a, str) and isinstance(b, str) and 
            set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'})):
        raise ValueError("Inputs must be strings consisting only of 1s and 0s")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the input strings
    for bit_a, bit_b in zip(a, b):
        # Perform XOR operation on corresponding bits
        result.append(str(int(bit_a) ^ int(bit_b)))

    # Join the result list into a string and return
    return ''.join(result)


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

Alternatively, you can use a more concise version of the function:

```python
def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the XOR operation as a binary string.
    """

    # Check if inputs are strings and contain only 1s and 0s
    if not (isinstance(a, str) and isinstance(b, str) and 
            set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'})):
        raise ValueError("Inputs must be strings consisting only of 1s and 0s")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be of the same length")

    # Use a generator expression to perform XOR operation and join the result into a string
    return ''.join(str(int(bit_a) ^ int(bit_b)) for bit_a, bit_b in zip(a, b))


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```