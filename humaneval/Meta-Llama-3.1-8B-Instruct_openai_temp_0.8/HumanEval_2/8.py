### Truncate Number Decimal Part

Below is a Python function that solves the problem by using the built-in `math.floor()` function to get the integer part of the number and then subtracting it from the original number to get the decimal part.

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part of the number.
    
    Args:
    number (float): A positive floating point number.
    
    Returns:
    float: The decimal part of the number.
    """
    
    # Get the integer part of the number using math.floor()
    integer_part = math.floor(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    # Return the decimal part
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
```

This script defines a function `truncate_number` that takes a float `number` as input and returns its decimal part. It uses the `math.floor` function to calculate the integer part of the number and then subtracts it from the original number to get the decimal part. Two example usage statements are provided to demonstrate how to use the function.