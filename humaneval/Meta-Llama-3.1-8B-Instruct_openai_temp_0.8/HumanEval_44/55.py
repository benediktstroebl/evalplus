```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of x in the target base.
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    nums = []
    while x:
        nums.append(digits[x % base])
        x //= base
    return ''.join(nums[::-1])

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. It uses a while loop to continuously divide `x` by `base` and append the remainder to the result list. The result list is then reversed and joined into a string. The script includes test cases to verify the correctness of the function.