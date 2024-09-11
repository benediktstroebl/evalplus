```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines the `truncate_number` function, which calculates the decimal part of a given number by subtracting the integer part from the original number. The `int(number)` function is used to get the largest integer smaller than the given number. The script then includes test cases to demonstrate the function's correctness.