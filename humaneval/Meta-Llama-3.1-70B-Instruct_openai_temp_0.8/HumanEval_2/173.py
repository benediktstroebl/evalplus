```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Number must be positive")

    # Use the modulo operator to get the decimal part
    # This works because the modulo operation returns the remainder of the division
    # of the number by 1, effectively removing the integer part
    decimal_part = number % 1

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```

Alternatively, you can use the `math.modf` function, which splits a number into its integer and fractional parts:

```python
import math

def truncate_number(number: float) -> float:
    if number < 0:
        raise ValueError("Number must be positive")

    _, decimal_part = math.modf(number)
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```