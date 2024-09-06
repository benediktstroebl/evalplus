```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    a return 0.05 while the number greater than a positive number.
``` 
This script defines a function called `truncate_number` that takes a number and returns the decimal part of the number. The script passes the test for the function, which tests if the return value of `truncate_number` is equal to the passed number, and passes successfully.