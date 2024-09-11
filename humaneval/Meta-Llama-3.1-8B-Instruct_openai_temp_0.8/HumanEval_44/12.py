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
        str: The string representation of the number in the new base.
    """
    if x < base:
        # If x is less than the base, return its string representation
        return str(x)
    else:
        # Otherwise, recursively convert x to the new base
        return change_base(x // base, base) + str(x % base)

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

However, a more efficient solution can be achieved by using the built-in `divmod` function and a loop:

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
        str: The string representation of the number in the new base.
    """
    if x < base:
        return str(x)
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```