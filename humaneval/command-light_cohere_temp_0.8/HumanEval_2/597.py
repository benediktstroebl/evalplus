```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 2.0
   
    arbitrary float value that can be represented using only
    positive integers and decimal values between 0 and 1.

    >>> test_truncate_number(10.5)
    random float that can be represented using only
    positive integers and decimal values between 0 and 1.
    """
    return 0.5 if number <1.0 else 1 decimal(number)
```