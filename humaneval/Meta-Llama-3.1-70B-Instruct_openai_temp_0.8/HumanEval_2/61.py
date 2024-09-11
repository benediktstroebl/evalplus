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
        raise ValueError("Input number must be positive")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines the `truncate_number` function as specified in the problem. It first checks if the input number is positive and raises a `ValueError` if it's not. It then calculates the integer part of the number by converting it to an integer, and calculates the decimal part by subtracting the integer part from the number. The function returns the decimal part. The example usage at the end demonstrates how to use the function with the provided test case.