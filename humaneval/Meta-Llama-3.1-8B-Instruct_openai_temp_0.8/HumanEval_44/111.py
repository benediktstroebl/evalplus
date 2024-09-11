```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to convert.
    base (int): The base to convert to. Base numbers are less than 10.
    
    Returns:
    str: The string representation of the number in the given base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns a string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the list of digits. Finally, it reverses the list and joins the digits into a string. The test cases are included to demonstrate the function's correctness.