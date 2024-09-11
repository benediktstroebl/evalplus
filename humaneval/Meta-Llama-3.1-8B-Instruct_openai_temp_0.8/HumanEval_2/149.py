```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    int_part = int(number)
    return number - int_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.8))  # Output: 0.8
print(truncate_number(7.23))  # Output: 0.23
```

This script defines the function `truncate_number`, which calculates the decimal part of a given positive floating point number by subtracting its integer part from the original number. It then includes three test cases to demonstrate the function's correctness.