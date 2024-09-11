```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target numerical base.
    
    Returns:
    str: The string representation of the number in the target base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9.")
    
    if x == 0:
        return '0'
    
    digits = "012345678"
    if base < 10:
        digits = digits[:base]
    
    result = ""
    while x:
        result = digits[x % base] + result
        x //= base
    
    return result


if __name__ == "__main__":
    print(change_base(8, 3))  # '22'
    print(change_base(8, 2))  # '1000'
    print(change_base(7, 2))  # '111'
```

This script defines the `change_base` function, which converts a given integer `x` to a specified base `base`. The function handles base conversion by repeatedly dividing the input number by the target base and appending the remainder to the result string, which is built in reverse order. If the base is less than 10, it uses a string of digits to avoid using indices that are out of range.