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

    Raises:
        ValueError: If the number is not a positive floating point number.
    """
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("Input must be a positive floating point number")

    # Calculate the integer part of the number
    integer_part = int(number)

    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The function first checks if the input is a positive floating point number. If not, it raises a `ValueError`. Then it calculates the integer part of the number by converting it to an integer. The decimal part is then calculated by subtracting the integer part from the number. Finally, the function returns the decimal part.

The script also includes an example usage of the function, which prints the decimal part of the number 3.5.