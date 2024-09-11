```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    # Use the math.floor function to truncate the number to the integer part
    truncated = math.floor(number)
    
    # Subtract the truncated integer part from the original number to get the decimal part
    decimal_part = number - truncated
    
    return decimal_part

import math

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
```

Note that this script uses the `math.floor` function from the math module, which is a built-in Python module. If you haven't imported the math module, you would need to add an import statement at the top of your script, which has been done in the above code.