```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Raises:
        ValueError: If the number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive")

    # Use the modulo operator to get the decimal part
    return number % 1


# Example use case:
if __name__ == "__main__":
    number = 3.5
    decimal_part = truncate_number(number)
    print(f"The decimal part of {number} is {decimal_part}")
```

This script defines the `truncate_number` function, which calculates the decimal part of a given positive floating point number. It uses the modulo operator (`%`) to get the remainder of the division by 1, which gives the decimal part.

It also includes a check to ensure the input number is positive and raises a `ValueError` otherwise.

In the example use case, the script demonstrates how to use the `truncate_number` function with a number `3.5`, and prints the result.