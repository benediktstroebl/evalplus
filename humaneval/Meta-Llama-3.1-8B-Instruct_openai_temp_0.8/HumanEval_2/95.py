```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Example use case:
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    return round((number - integer_part), 10)  # Round to 10 decimal places to ensure accuracy

# Testing the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.75))  # Output: 0.75
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating-point number as input, calculates the integer part and the decimal part, and returns the decimal part. The decimal part is calculated by subtracting the integer part from the input number and rounding the result to 10 decimal places to ensure accuracy. The function is then tested with different inputs to demonstrate its correctness.