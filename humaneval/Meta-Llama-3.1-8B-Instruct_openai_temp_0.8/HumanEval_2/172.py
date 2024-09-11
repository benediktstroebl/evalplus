```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5

    :param number: A positive floating point number
    :return: The decimal part of the number
    """
    return number - int(number)


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5.0))  # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as an argument and returns its decimal part. It does this by subtracting the integer part (obtained by casting the number to an integer) from the original number. The function is then tested with three examples to ensure it's working as expected.