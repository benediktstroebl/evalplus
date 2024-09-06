```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.3
   
    Warren E. shortening below test main function of passing a floating point number as an argument, and returning the decimal part of the number. The function is well-contained and self-contained, as it has only one operation (returning the decimal part) and passes all the tests.