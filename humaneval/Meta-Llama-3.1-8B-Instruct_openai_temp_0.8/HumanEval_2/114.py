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
    # Use the math.modf function to decompose the number into its integer and decimal parts
    from math import modf
    # The decimal part is the second element of the tuple returned by modf
    decimal_part, _ = modf(number)
    return decimal_part

# Test the function with some examples
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(2.0))  # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a floating point number as input and returns its decimal part. The decimal part is obtained by using the `math.modf` function, which decomposes the number into its integer and decimal parts. The decimal part is then returned by the function. The script also includes some example use cases to demonstrate the function's behavior.