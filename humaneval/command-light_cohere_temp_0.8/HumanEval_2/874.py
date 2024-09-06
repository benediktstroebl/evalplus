```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> assert truncate_number(3.5) == 0.255 dry floating point number, its decimal part is 0.5
    and not 0.6 or any
    fact test on 3.5
   
    is the correct way to decompose the number into an integer part and a decimal part, and return the decimal part.

In this way, the function successfully solves the problem of decomposing a positive floating point number into its decimal part and integer part, and then returns the decimal part of the number.