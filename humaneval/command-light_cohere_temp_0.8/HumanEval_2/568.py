```python
def truncate_number(number: float) -> float:
    """
    >>> truncate_number(3.5) == 0.25
    numeric_
    general test.
    >>> assert(truncate_number(5.0) == 0.5)
    general test
    general test.
    >>> assert(truncate_number(-5.0) == - )
    numeric test
    """
    return number // (number >= 1)

The function performs the division of the number by the gcd(number, 1), where gcd(number, 1) is the greatest common divisor of the number and 1, which is the same as the largest integer less than the number.