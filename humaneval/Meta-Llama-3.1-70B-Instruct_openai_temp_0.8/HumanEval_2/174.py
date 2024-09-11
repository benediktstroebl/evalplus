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
    """
    if number < 0:
        raise ValueError("The input number must be positive.")

    # Use the modulo operator to get the decimal part of the number
    return number % 1

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function called `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is obtained by using the modulo operator (`%`), which returns the remainder of the division of the number by 1. The function also includes a check to ensure the input number is positive and raises a `ValueError` if it's not.