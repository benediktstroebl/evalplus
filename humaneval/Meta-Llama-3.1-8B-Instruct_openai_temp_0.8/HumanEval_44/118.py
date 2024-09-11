```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    """
    # Check if base is valid
    if not 2 <= base <= 9:
        raise ValueError("Base should be an integer between 2 and 9")

    # Convert to base
    converted = ""
    while x > 0:
        converted = str(x % base) + converted
        x = x // base

    return converted


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function to convert a number `x` from base 10 to a given base `base`. It checks if the base is valid before proceeding, and uses the modulo operator (`%`) and integer division (`//`) to perform the conversion. The test cases at the end demonstrate the function's behavior for different inputs.