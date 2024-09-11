```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Use the zip function to iterate over the characters in both strings
    # simultaneously, and use a list comprehension to apply the XOR operation
    # (which is equivalent to a ^ b in binary)
    result = ''.join('1' if c1!= c2 else '0' for c1, c2 in zip(a, b))
    
    return result


# Test the function with an example
if __name__ == "__main__":
    a = '010'
    b = '110'
    print(f"xor of {a} and {b} is {string_xor(a, b)}")
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, performs binary XOR operation on them, and returns the result as a string. The function uses a list comprehension with the `zip` function to iterate over the characters in both strings simultaneously, and a conditional expression to apply the XOR operation. The result is then joined into a string using the `join` method. The script also includes a test case to demonstrate the usage of the function.