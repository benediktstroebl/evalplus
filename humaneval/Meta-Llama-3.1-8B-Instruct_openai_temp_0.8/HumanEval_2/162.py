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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the integer part of the number using the math.floor function
    import math
    integer_part = math.floor(number)
    
    # Calculate the decimal part of the number by subtracting the integer part from the original number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.123))  # Output: 0.123
```

This script defines a function `truncate_number` that calculates the decimal part of a given number. It uses the `math.floor` function to calculate the integer part and then subtracts this from the original number to get the decimal part. The function includes a docstring that describes its purpose, parameters, and return values. Lastly, it includes some test cases to demonstrate its usage.