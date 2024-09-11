```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, returns the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    
    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.3))  # Expected output: 0.3
print(truncate_number(10.0)) # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number (obtained using `int(number)`) from the number itself. The function is then tested with a few examples to demonstrate its correctness.