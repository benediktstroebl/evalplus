```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
    a (str): First binary string consisting only of 1s and 0s.
    b (str): Second binary string consisting only of 1s and 0s.

    Returns:
    str: Result of binary XOR operation as a string.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Use a list comprehension to perform XOR operation on corresponding bits
    result_list = [str(int(a[i]) ^ int(b[i])) for i in range(len(a))]

    # Join the result list into a string
    return ''.join(result_list)


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function, which takes two binary strings as input and returns their XOR result as a string. It checks if both strings have the same length and then performs the XOR operation using a list comprehension. The result is then joined into a string and returned.

The example usage demonstrates how to call the `string_xor` function with two binary strings and print the result.