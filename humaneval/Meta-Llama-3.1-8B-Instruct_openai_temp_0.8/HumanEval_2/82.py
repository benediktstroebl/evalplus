### Truncate Number into Decimal Part

Here's a Python function that uses math.floor to get the integer part and then subtracts the integer part from the given number to get the decimal part:

```python
import math

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Check if number is a positive float
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input number must be a positive float")

    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - math.floor(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.0))  # Output: 0.0
print(truncate_number(5.7))  # Output: 0.7
```

This function takes a positive floating point number as an argument, subtracts its integer part from it to get the decimal part, and then returns the decimal part. 

It first checks if the input number is a positive float. If not, it raises a ValueError. The integer part is calculated using math.floor(number), which returns the largest integer smaller than or equal to the given number. The decimal part is then calculated by subtracting the integer part from the number. 

Finally, it returns the decimal part.