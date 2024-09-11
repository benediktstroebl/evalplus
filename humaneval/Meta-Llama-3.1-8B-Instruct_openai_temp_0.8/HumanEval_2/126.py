### Truncate Number Function
#### Problem Statement
Given a positive floating point number, decompose it into an integer part and decimals.
Return the decimal part of the number.

#### Solution
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
    # Use the built-in floor function from math module to get the largest integer smaller than the number
    import math
    integer_part = math.floor(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It uses the `math.floor` function to get the largest integer smaller than the input number, and then calculates the decimal part by subtracting the integer part from the input number. The script also includes example use cases to demonstrate the function's behavior.