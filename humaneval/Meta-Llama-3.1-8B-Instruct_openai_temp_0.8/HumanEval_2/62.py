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
print(truncate_number(4.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```
This Python script defines a `truncate_number` function that takes a floating point number as input and returns its decimal part. It uses the fact that subtracting the integer part of a number from the number itself effectively removes the integer part, leaving only the decimal part. The function is then tested with a few examples to demonstrate its correctness.