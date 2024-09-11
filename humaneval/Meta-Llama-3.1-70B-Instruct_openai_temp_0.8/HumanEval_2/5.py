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
    # Ensure the number is positive
    if number < 0:
        raise ValueError("Input number must be positive.")

    # Calculate the integer part by converting to int
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

Alternatively, you can use the built-in `math.modf()` function, which returns a tuple of the fractional and integer parts of a number.

```python
import math

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
    # Ensure the number is positive
    if number < 0:
        raise ValueError("Input number must be positive.")

    # Calculate the decimal part using math.modf()
    decimal_part, _ = math.modf(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```