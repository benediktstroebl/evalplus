```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage
print(truncate_number(3.5))  # Output: 0.5
```

This script works by simply subtracting the integer part of the number from the number itself. The integer part is obtained using the built-in `int()` function, which truncates the decimal part of the number.

Alternatively, you can also use the modulo operator (`%`) to get the decimal part:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1

# Example usage
print(truncate_number(3.5))  # Output: 0.5
```

This approach works because the modulo operator returns the remainder of the division of the number by 1, which is essentially the decimal part of the number.