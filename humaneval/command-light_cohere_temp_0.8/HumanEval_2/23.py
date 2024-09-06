```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).
    >>> print(truncate_number(3.5))
    0.05
    ```
    lowest integer smaller than the given number is 2,
        so it will return 0.0

    """
    test that passes the function is below:
    >>> test_pass = True
    >>> truncate_number(3.5) == 0.05
    test pass
    TUPED out to test_test_pass == True

This Python script defines a function called `truncate_number` that takes a float number as input and returns the decimal part of the number. The function uses the positive float number as input and returns the decimal part of the number.

The decimal part is the part of the number that is less than 1. It can be decomposed into the integer part (the largest integer that is less than the given number) and the decimal part (the leftover part, which is always less than 1). The function returns the decimal part of the number.

The script also includes a test that checks if the function is working correctly.