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
    if number < 0:
        raise ValueError("Input number must be a positive floating point number.")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part of the number
    decimal_part = number - integer_part
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```

Alternatively, you can also use the built-in `math.modf` function, which returns a tuple containing the fractional and integer parts of a number:

```python
import math

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
    if number < 0:
        raise ValueError("Input number must be a positive floating point number.")

    # Calculate the decimal part of the number
    decimal_part, _ = math.modf(number)
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
```