```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part
    integer_part = int(number)

    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.123))  # Output: 0.123
```

Alternatively, you can use the built-in `math.modf` function which returns a tuple containing the fractional and integer parts of the number.

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Use math.modf to get the fractional part
    _, decimal_part = math.modf(number)

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.123))  # Output: 0.123
```