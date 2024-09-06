```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5)
   0.10000004
    extremely small number (use this function)
    """
    return 1e-10 ** (number - 1) // 10

# More test cases:
# Now test large numbers.
# Test floating numbers.
print(truncate_number(1e12))
print(truncate_number(1e-10))
print(truncate_number(-1e-10))
print(truncate_number(3.5))
print(truncate_number(3.5e))
print(truncate_number(1))
print(truncate_number(0))
print(truncate_number(-0))
```
This code defines a function `truncate_number` that takes a floating point number as an argument and returns the decimal part of the number, effectively truncating the floating-point number to a decimal number.

The function uses the formula `1e-10 * (number - 1) / 10` to calculate the decimal part of the number, where `1e-10` is a constant representing 10 raised to the power of 10, and `(number - 1)` is a formula for subtracting the floor from a number.

This formula effectively removes the decimal part of the number by dividing the floor of the number by 10, which results in a fractional value between 0 and 1 representing the decimal part of the number.

This is a common technique used in many mathematical and scientific computing applications to remove decimal parts from floating-point numbers and return the integer part of the number, which is more easily stored and manipulated in many computer systems.