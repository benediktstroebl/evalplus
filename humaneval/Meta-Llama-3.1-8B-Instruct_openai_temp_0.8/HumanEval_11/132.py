```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.

    Returns:
        str: The result of binary XOR operation on inputs a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Perform XOR operation
    result = int_a ^ int_b

    # Convert result back to binary and remove '0b' prefix
    return bin(result)[2:]


if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: 100
```

In this script, we first check if the input strings consist only of 1s and 0s. If not, we raise a ValueError. Then we convert the binary strings to integers using the built-in int function with base 2. We perform the XOR operation on these integers and convert the result back to binary using the bin function. The [2:] is used to remove the '0b' prefix that Python adds to binary numbers.