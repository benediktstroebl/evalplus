```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    """
    # Implementation of the above function:
    integer, decimal = divmod(number, 10)
    return float('{:0.0f5 number decimal')
```

This function takes a number as input and returns the decimal part of that number. The function uses the 'divmod' function to get the integer and decimal parts of the number.