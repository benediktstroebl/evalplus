```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
    number (float): A positive floating point number

    Returns:
    float: The decimal part of the number
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part
    integer_part = int(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```

Alternatively, you can also use the built-in `math.modf()` function in Python to achieve the same result:

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
    number (float): A positive floating point number

    Returns:
    float: The decimal part of the number
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Use math.modf() to split the number into integer and decimal parts
    _, decimal_part = math.modf(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```