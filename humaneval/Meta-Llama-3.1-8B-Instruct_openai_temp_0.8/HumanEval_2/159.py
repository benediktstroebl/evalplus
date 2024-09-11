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
print(truncate_number(2.0))  # Output: 0.0
print(truncate_number(1.7))  # Output: 0.7
```

In this code, we subtract the integer part of the number (`int(number)`) from the original number (`number`). This effectively gives us the decimal part because any integer is an exact multiple of 1. So, in other words, the integer part of a number is the biggest multiple of 1 that is smaller or equal to the number, and the decimal part, by definition, must be zero or smaller.