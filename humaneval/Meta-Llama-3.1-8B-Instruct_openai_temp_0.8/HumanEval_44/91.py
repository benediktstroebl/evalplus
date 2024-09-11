```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): Input number
    base (int): Target base (less than 10)

    Returns:
    str: String representation of the number in the target base
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be integers")
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return '0'
    digits = "012345678"
    result = ""
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script provides a function `change_base()` that takes an integer `x` and a base `base` as input. It converts the number `x` to the target base and returns the string representation of the number. The function includes input validation to ensure that both `x` and `base` are integers and that the base is between 2 and 9 (inclusive). The script also includes test cases to demonstrate the correctness of the function.