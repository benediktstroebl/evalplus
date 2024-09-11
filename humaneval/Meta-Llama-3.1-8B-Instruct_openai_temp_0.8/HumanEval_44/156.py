```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.

    Args:
    x (int): The number to be converted.
    base (int): The target base (less than 10).

    Returns:
    str: String representation of the number in the target base.
    """
    if x == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a while loop to repeatedly divide the input number `x` by the target base `base` and append the remainder to the result string. The remainder is obtained using the modulo operator (`x % base`). The division operation is performed using integer division (`x //= base`) to ensure that the result is an integer. The digits used in the conversion are defined in the `digits` string. The function returns the result string in reverse order.