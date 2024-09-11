```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to which the number should be converted.
    
    Returns:
    str: The string representation of the number in the new base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # Should print: '22'
print(change_base(8, 2))  # Should print: '1000'
print(change_base(7, 2))  # Should print: '111'
```

This script works by recursively dividing the input number by the base and prepending the remainder to the result. If the remainder is less than the base, it simply converts the remainder to a string and returns the result. This process continues until the input number is less than the base. The final result is a string representation of the number in the desired base.