```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: int, numerical number
    :param base: int, base to convert to
    :return: string representation of x in base base base
    """
    if x < 0:
        raise ValueError("Cannot convert negative numbers to positive bases")
    # convert x to string representation in decimal
    # convert decimal to string representation in base base
    # convert string representation back to int (change base)
    return '{:b}'.format(int(x, base))

# tests
test_positive = change_base(7, 10)
print("Test Positive:", test_positive)

test_negative = change_base(-7, 10)
print("Test Negative:", test_negative)

test_zero = change_base(0, 10)
print("Test Zero:", test_zero)

test_large = change_base(123456789, 2)
print("Test Large:", test_large)
``` 
This code defines a function `change_base` that converts a given number to a string representation in a specified base. It uses the Python's `int` function to convert the number to a string representation in decimal, then converts the decimal to a string representation in the specified base, and finally converts the string representation back to an int (changing the base).

This code also contains several tests for the `change_base` function to ensure it is working correctly.