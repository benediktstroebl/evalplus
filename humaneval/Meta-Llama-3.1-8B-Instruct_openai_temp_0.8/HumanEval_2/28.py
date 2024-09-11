```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```

In this script, the `truncate_number` function subtracts the integer part of the input number from the original number. This is based on the fact that `int(number)` gives the largest integer smaller than the given number. The result is the decimal part of the number. 

Note that this function assumes that the input number is positive. If the input number can be negative or zero, you should add error checking code to handle these cases.