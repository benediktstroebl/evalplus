```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2
   
   0
5
    """If the number is negative, return 0.0, otherwise, return the number itself."""

This code defines a function that takes a floating-point number as input and returns the decimal part of that number. It can be used to decompose a number into its integer and decimal parts and return the decimal part of the number.