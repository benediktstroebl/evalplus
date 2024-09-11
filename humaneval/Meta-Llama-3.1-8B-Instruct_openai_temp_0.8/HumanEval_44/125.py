### Change Numerical Base of a Number
#### Problem Description
Convert a number from a given base to a specified base (between 2 and 9).

#### Solution
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to convert.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers.")
    if not (2 <= base < 10):
        raise ValueError("Base must be between 2 and 9.")
    
    if x < base:
        return str(x)
    
    digits = '0123456789'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x = x // base
    
    return result

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

In this script, the `change_base` function converts the given number `x` to the target base by repeatedly applying the modulo operator and integer division. The result is a string representing the number in the target base.