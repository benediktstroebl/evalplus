```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base (less than 10).
    
    Returns:
        str: The string representation of the number in the target base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses recursion to convert the input number `x` from decimal to the target base. It works by repeatedly dividing the number by the base and appending the remainder to the result string. When the number is less than the base, it simply converts it to a string and returns it.