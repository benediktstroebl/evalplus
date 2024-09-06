```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    integral part is the leftover is 1e-5e (10), which is smaller than the target.
    >>> truncate_number(0.000f) is the integral part is 0
    >>> truncate_number(-3.5) is integral part is also -1e-5e (10), which is smaller than the target
    >>> assert truncate_number(3.5) == 1ee
    integral part is 0
    >>> assert truncate_number(-3.5) == - integral part is -1e-5e (10), which is smaller than the target
    """