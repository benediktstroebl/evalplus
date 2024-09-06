```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.5
   
    important floating point number is the decimal part will always be a
    finite number less than 1. The function uses the mathematical function to divide
    the number by 10^9 and returns the decimal part.

This code is a self-contained solution to the problem you have outlined.