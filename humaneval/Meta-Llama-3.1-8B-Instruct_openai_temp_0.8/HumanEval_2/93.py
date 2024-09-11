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

    Raises:
        ValueError: If the input number is not a positive floating point number.
    """
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("Input number must be a positive floating point number.")
    
    # Separate the integer and the decimal part using the modulo operator
    integer_part = int(number)
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This Python script contains a function `truncate_number` that takes a float number as input, calculates its decimal part, and returns it. It includes input validation to ensure the number is positive and a float. The example usage at the end demonstrates how to call the function with a sample input.