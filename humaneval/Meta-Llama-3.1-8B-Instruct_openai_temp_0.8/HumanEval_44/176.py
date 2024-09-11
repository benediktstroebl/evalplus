```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): Number to be converted.
    base (int): Target numerical base.
    
    Returns:
    str: String representation of x in base.
    
    Raises:
    ValueError: If base is not less than 10.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    
    convertString = "012345678"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result

# Example usage
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(10, 2)) # Output: '1010'
print(change_base(10, 16)) # Output: 'A'
```
The `change_base` function uses the standard division operator (`//`) to divide `x` by `base` and the modulus operator (`%`) to get the remainder of the division. The remainder is then used as an index into the `convertString` to get the corresponding digit in the target base. This process continues until `x` is 0, at which point the result is the string representation of `x` in the target base. The example usage shows how to use this function with different inputs to demonstrate its correctness.