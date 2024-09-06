Here is a self-contained Python script that defines a function that solves the problem of truncating a given positive floating point number to a decimal part:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.255 mere decimal number: 
    >>> truncate_number(1234567) == 34567
    """
    return number - (number ** 0.0128)