```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Outputs: 0.5
```

This script defines a function `truncate_number` that takes a floating point number as input and returns its decimal part. The function works by subtracting the integer part of the number (obtained using the `int()` function) from the original number. The result is the decimal part of the number.

You can run this script and test the function with different inputs to see that it works as expected.