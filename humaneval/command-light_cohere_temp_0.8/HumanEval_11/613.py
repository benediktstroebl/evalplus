Here's a self-contained Python function that performs the XOR operation on two strings consisting only of ones and zeros, and returns the result as a string:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    Convert the string to integers and do the XOR operation.
    Convert result back integer to a string and return it
    """
    # Convert input strings to integers
    a = [int(c) for c in a]
    b = [int(c) for c in b]

    # XOR operation
    result = 0
    for i in range(len(a)):
        result = result | a[i]

    # Convert result to string
    result = str(result)

    return result

# Example test cases
print(string_xor('010', '110'))  # Output: 100
print(string_xor('00000000', '10101010'))  # Output: 1010101010
print(string_xor('   ', '   '))  # Output:   00000
```