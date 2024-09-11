```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    return number - integer_part

# Testing the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(10.25))  # Expected output: 0.25
```

This script defines the `truncate_number` function, which takes a positive floating point number as input, calculates its integer part using the built-in `int` function, and then returns the decimal part by subtracting the integer part from the original number. The script also includes some test cases to demonstrate the function's behavior.