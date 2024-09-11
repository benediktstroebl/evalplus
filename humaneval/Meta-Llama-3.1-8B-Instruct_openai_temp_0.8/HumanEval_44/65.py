```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to convert.
    base (int): The target base (less than 10).
    
    Returns:
    str: The string representation of x in the target base.
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

This script uses a recursive approach to convert the number to the target base. The base case of the recursion is when the number is less than the target base, in which case it simply converts the number to a string. Otherwise, it recursively converts the quotient of the number divided by the base and appends the remainder as a string.