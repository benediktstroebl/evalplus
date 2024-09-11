```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.8))  # Output: 0.8
print(truncate_number(7.2))  # Output: 0.2
```

In this script, we use the fact that the `int()` function truncates the decimal part of a number and returns the integer part. By subtracting the integer part from the original number, we get the decimal part.

Alternatively, you can use the `math.modf()` function, which splits a number into its integer and fractional parts:

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return math.modf(number)[0]

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.8))  # Output: 0.8
print(truncate_number(7.2))  # Output: 0.2
```

In this version, `math.modf(number)[0]` returns the fractional part of the number.