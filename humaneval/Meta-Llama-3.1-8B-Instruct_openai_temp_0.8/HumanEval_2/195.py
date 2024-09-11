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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in int function to get the largest integer smaller than the given number
    # Then subtract this integer from the number to get the decimal part
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
```

This script defines a function `truncate_number` that takes a floating point number as input and returns its decimal part. It uses the built-in `int` function to truncate the number to the nearest integer, and then subtracts this integer from the original number to get the decimal part. The script also includes some test cases to demonstrate the function's behavior.