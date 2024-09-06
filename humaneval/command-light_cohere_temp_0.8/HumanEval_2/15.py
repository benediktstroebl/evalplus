```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    example""" decimal part of the number is 3.5 is exactly the same as the integer part.
    """ The original code:

This code defines a function `truncate_number` which takes a float number as input and returns the decimal part of the number. 

The function uses the concept of the decimal representation of a floating point number, where the decimal part is always less than 1 and the integer part is the largest integer less than the number.