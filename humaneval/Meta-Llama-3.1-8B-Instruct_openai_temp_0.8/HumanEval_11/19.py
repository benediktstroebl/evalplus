### Binary String XOR
#### A Python Script to Perform Binary XOR on Two Binary Strings

```python
def string_xor(a: str, b: str) -> str:
    """ 
    Perform binary XOR on two binary strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")

    # Use a list comprehension to perform XOR on corresponding bits
    result = ['1' if x!= y else '0' for x, y in zip(a, b)]

    # Join the result list into a string
    return ''.join(result)

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR on them, and returns the result as a string. The function first checks if both strings have the same length, and if not, it raises a `ValueError`. Then it uses a list comprehension to perform XOR on corresponding bits of the two strings, and finally joins the result list into a string. The example usage at the end demonstrates how to use the function.