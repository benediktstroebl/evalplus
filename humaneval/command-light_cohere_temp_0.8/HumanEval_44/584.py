```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another.
    :param x: int -- Input number to be base converted
    :param base: int -- Conversion base
    :return: string representation after base change
    """
    assert isinstance(x, int) and x >= 0, "Input number should be non-negative integer"
    assert isinstance(base, int) and base > 0 and base <= 36, "Base should be a positive integer less than 37"

    # Handle non-integer input and negative base case
    if not isinstance(x, int) or x < 0:
        raise TypeError("Input must be a non-negative integer")

    # Handle invalid base case
    if base > 37:
        raise ValueError("Base cannot be greater than 37")

    # Convert and return string representation
    return format(x, '{:{}b}'.format(base), '>').

# Test case 1
print(change_base(8, 3))
# Expected output: '22'

# Test case 2
print(change_base(-8, 3))
# Expected output: '22'

# Test case 3
print(change_base(7, 2))
# Expected output: '111'

# Test case 4
print(change_base(9, 16))
# Expected output: '9888'
```
This Python code provides a function called `change_base` which converts a given number to a specified base. It ensures that the valid input types and range of base values are checked. The `assert` statements are used to validate the input and base, raising appropriate exceptions if the conditions are not met. The code also includes several test cases to verify the correctness of the `change_base` function.