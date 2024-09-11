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
        ValueError: If the input number is not a positive float.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive float.")

    integer_part = int(number)
    decimal_part = number - integer_part

    return decimal_part


# Example usage:
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.25))  # Output: 0.25
```

In this code:

*   We define the `truncate_number` function with a docstring that describes its purpose, arguments, return value, and raises.
*   We check if the input is a positive float. If not, we raise a `ValueError`.
*   We calculate the integer part by converting the number to an integer using `int(number)`.
*   We calculate the decimal part by subtracting the integer part from the original number.
*   In the `if __name__ == "__main__":` block, we provide example usage of the function.