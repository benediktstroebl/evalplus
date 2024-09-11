```markdown
### Change Base Function
#### Description
This function takes an integer `x` and a base `base` as input and returns the string representation of `x` in the specified base.

#### Code
```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base. Should be less than 10.
    
    Returns:
        str: The string representation of x in the base.
    
    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(str(digit) for digit in reversed(digits))
```

#### Usage
```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
```