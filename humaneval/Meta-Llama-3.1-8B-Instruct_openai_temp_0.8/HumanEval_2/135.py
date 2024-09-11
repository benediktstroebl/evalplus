### Truncate Number to Decimal Part
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part.
    
    The number is decomposed into an integer part (largest integer smaller than given number) and decimals.
    The decimal part is always smaller than 1.
    
    Parameters:
    number (float): A positive floating point number.
    
    Returns:
    float: The decimal part of the number.
    """
    return number - int(number)

# Example use cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.2))  # Expected output: 0.2
print(truncate_number(10.0))  # Expected output: 0.0
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is calculated by subtracting the integer part of the number from the original number. The example use cases demonstrate the function's usage with different inputs.