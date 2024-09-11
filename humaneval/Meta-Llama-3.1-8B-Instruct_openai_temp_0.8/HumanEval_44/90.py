```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number after conversion.
    """
    if not 2 <= base <= 10:
        raise ValueError("Base numbers are less than 10")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x < base:
        return digits[x]
    
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that converts a number `x` from base 10 to a specified base `base`. It uses a string `digits` to map numbers to their corresponding digits in the new base. If the number `x` is less than the base `base`, it returns the corresponding digit. Otherwise, it repeatedly divides `x` by `base` and prepends the remainder to the result string. The function returns the result string after the conversion.