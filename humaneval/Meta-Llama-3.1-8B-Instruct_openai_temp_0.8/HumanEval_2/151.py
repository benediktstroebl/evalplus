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
        float: The decimal part of the given number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the integer part using the math.floor function
    import math
    integer_part = math.floor(number)
    
    # Return the decimal part by subtracting the integer part from the original number
    return number - integer_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.99))  # Expected output: 0.99
print(truncate_number(5.0))  # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating-point number as input, calculates its decimal part, and returns it. The function uses the `math.floor` function to find the largest integer smaller than the input number, then subtracts this integer from the original number to get the decimal part. The script includes docstrings to document the function's behavior and example use cases, as well as test cases to verify its correctness.