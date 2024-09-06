```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.5
   
    facinating that integer part of 3.5 is 3, while the fractional part is 5.
    >>> truncate_number(-0.5) == -5
    facinating the integer part of -0.5 is 5, while the fractional part is -5.
    >>> truncate_number(float("inf")) == float("1")
    >>> truncate_number(float("1.5")) == float("1")
    """