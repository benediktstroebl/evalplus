```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.0

   _float_1584f
   

Test cases:
>>> assert truncate_number(3.5) == 0.0
>>> assert truncate_number(-3.5) == -inf

>>> assert truncate_number(1) == 1
>>> assert truncate_number(10) == 5.0

>This script defines a function `truncate_number` that takes a float number as input and returns the decimal part of the number as a float.