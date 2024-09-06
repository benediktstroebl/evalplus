```python
def truncate_number(n: float) -> float:
    """Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number."""

    return (n // int(n))  # integer part + (fract(...) * 1)

# Example of passing test
test_truncate_number(3.5)
```

This Python code defines a function `truncate_number` that takes a floating-point number as input and returns the decimal part of that number. 

The function uses the division by integer conversion to extract the integer part of the number, and then adds the result of multiplying the fractional part by 1 to the integer part to return the decimal part of the number.