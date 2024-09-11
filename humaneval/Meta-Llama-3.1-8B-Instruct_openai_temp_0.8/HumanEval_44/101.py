```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: The number to convert
    :type x: int
    :param base: The base to convert to
    :type base: int
    :return: String representation of the converted number
    :rtype: str
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers")
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))   # Outputs: 22
print(change_base(8, 2))   # Outputs: 1000
print(change_base(7, 2))   # Outputs: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the given base. The function first checks if both inputs are integers and the base is within the valid range (between 2 and 9). It then converts the number to the desired base by repeatedly taking the remainder when the number is divided by the base, and prepending this remainder to the result. Finally, it returns the string representation of the result. The test cases at the end verify the function's correctness.