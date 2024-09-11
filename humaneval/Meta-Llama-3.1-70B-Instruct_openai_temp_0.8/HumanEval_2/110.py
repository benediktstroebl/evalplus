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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative float")
    
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # The decimal part is the number minus its integer part
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

Alternatively, you can also use the `math.modf()` function which returns a tuple containing the fractional and integer parts of a number:

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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative float")
    
    # Calculate the decimal part of the number
    _, decimal_part = math.modf(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```