```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
   
    The decimal part is always smaller than the original number.

    Return the decimal part of the number
    >>> truncate_number(3.5)
    0.4
   
    important
    region, only integers are accepted
    >>> int(truncate_number(3.6))
    3

    The test passes because 3.6 has a important integer value of 3.

Please note that this implementation assumes that the input number is always positive. It may not work correctly for negative numbers or non-floating-point numbers.