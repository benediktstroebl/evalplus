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
        float: The decimal part of the input number.
    """
    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(9.99))  # Output: 0.99
print(truncate_number(2.0))   # Output: 0.0
```

This script defines the `truncate_number` function that takes a positive floating point number, subtracts its integer part to get the decimal part, and returns it. The function then tests this with some examples. 

The `int(number)` function is used to get the largest integer smaller than the input number. The difference between the input number and this integer is the decimal part, as required by the problem.