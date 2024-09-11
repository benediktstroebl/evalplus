```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): Input number.
        base (int): Desired base for the output number.

    Returns:
        str: String representation of the input number in the desired base.
    """
    if not 2 <= base <= 10:
        raise ValueError("Base must be between 2 and 10")

    # Handle the case when x is 0
    if x == 0:
        return '0'

    digits = "0123456789"
    result = ""

    while x:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result

    return result

# Test cases
print(change_base(8, 3))   # Outputs: 22
print(change_base(8, 2))   # Outputs: 1000
print(change_base(7, 2))   # Outputs: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `b`, converts `x` to base `b`, and returns the result as a string. It uses the `divmod` function to get the quotient and remainder when `x` is divided by `b`. The remainder is used to get the corresponding digit from the string "0123456789". The result is built from left to right by prepending each new digit to the result string.