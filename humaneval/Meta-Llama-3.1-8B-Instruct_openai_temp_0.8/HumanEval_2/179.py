```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.7))  # Outputs: 0.7
```

This Python script defines a function `truncate_number` that takes a floating-point number and returns its decimal part. It works by subtracting the integer part of the number (obtained using the `int()` function) from the original number. The example usage section demonstrates how to use the function with different inputs.