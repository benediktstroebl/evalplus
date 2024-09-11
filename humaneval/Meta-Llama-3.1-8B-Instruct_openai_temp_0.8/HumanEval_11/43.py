```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if set(a).issubset('10') and set(b).issubset('10'):
        return ''.join('1' if c!= d else '0' for c, d in zip(a, b))
    else:
        raise ValueError("Input strings must consist only of 1s and 0s")


def main():
    # Test the function
    print(string_xor('010', '110'))  # Expected output: '100'
    try:
        print(string_xor('abc', '110'))  # Expected exception
    except ValueError as e:
        print(e)  # Expected output: Input strings must consist only of 1s and 0s


if __name__ == "__main__":
    main()
```

In this script, the `string_xor` function takes two input strings, performs binary XOR on them, and returns the result as a string. It first checks if the input strings consist only of 1s and 0s. If they do, it performs the XOR operation by comparing corresponding characters and returning the result as a string. If the input strings do not meet the condition, it raises a ValueError. The `main` function tests the `string_xor` function with a valid input and an invalid input that raises a ValueError.