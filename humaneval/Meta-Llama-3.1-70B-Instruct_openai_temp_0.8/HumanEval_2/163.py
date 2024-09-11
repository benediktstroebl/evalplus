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
        ValueError: If the input number is not positive.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    if number <= 0:
        raise ValueError("Input number must be positive.")

    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    return decimal_part

# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating-point number as input and returns its decimal part. The decimal part is calculated by subtracting the integer part of the number from the number itself. The function includes a check to ensure the input number is positive and raises a `ValueError` otherwise. The script also includes an example usage in the `if __name__ == "__main__":` block.