```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base.
    
    Returns:
        str: String representation of the number in the target base.
    
    Notes:
        The target base must be less than 10.
    """
    if not 2 <= base <= 9:
        raise ValueError("Target base must be between 2 and 9.")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Convert the list of digits back to a string, but in reverse order
    return ''.join(map(str, digits[::-1]))


# Example usage
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

This Python script defines the `change_base` function, which takes an integer `x` and a target base as arguments and returns the string representation of `x` in the target base. The function uses a while loop to repeatedly divide `x` by the target base, appending the remainder to the result list. The result list is then reversed and converted back to a string for output.