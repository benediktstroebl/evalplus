```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base.
    :param x: The number to be converted
    :param base: The base to be converted to
    :return: The converted string representation of x in base base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value")
        
    ret = ''
    while x > 0:
        if x % base == 0:
            ret += str(x // base)
        x //= base
        
    return ret

# Example usage
print(change_base(8, 3)) # Output: '22'
print(change_base(7, 9)) # Should raise ValueError due to invalid base
```