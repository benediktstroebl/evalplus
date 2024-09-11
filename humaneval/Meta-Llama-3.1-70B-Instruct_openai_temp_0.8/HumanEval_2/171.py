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

    # Calculate the integer part using the math.floor function
    import math
    integer_part = math.floor(number)

    # Calculate the decimal part by subtracting the integer part from the original number
    decimal_part = number - integer_part

    return decimal_part

# Example use case:
number = 3.5
print(truncate_number(number))  # Output: 0.5
```