```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The numerical base to convert to.
    
    Returns:
    str: The string representation of the number in the new base.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9.")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))

# Example usage:
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This script provides a function `change_base` that takes an integer `x` and a base `base` as input. It then converts the number `x` to the new base and returns the result as a string. The script handles cases where the input number is 0 and also includes input validation to ensure that both `x` and `base` are integers and that `base` is between 2 and 9 (inclusive).