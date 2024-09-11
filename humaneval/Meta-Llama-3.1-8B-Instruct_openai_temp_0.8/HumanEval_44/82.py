```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The base to which x should be converted.
        
    Returns:
        str: String representation of x in the specified base.
        
    Raises:
        ValueError: If base is not less than 10.
    
    Example:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base should be less than 10")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This Python script defines a function `change_base` that takes two integer arguments: the number to be converted (`x`) and the base to which it should be converted (`base`). It uses a recursive approach to convert the number to the specified base. If the base is less than 2 or greater than or equal to 10, it raises a `ValueError`. It returns the string representation of `x` in the specified base. The script includes example use cases at the end.