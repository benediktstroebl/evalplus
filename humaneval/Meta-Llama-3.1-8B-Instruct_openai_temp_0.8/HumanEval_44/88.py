### Base Conversion Script
```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Returns string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): The input number to be converted.
        base (int): The base to which the number should be converted (less than 10).
    
    Returns:
        str: The string representation of the number in the given base.
    """
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9")

    convertString = "0123456789"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This script defines a function `change_base` that takes an integer `x` and a base `base` as input, converts `x` to the given base, and returns the result as a string. The function uses a while loop to repeatedly divide the input number by the base and append the remainder to the result string. The remainder is obtained by taking the modulus of the input number with the base. The process continues until the input number becomes 0. The result string is constructed by appending the remainder to the beginning of the result string. The function also includes a check to ensure that the base is between 2 and 9.