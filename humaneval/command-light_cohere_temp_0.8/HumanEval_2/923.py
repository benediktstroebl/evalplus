```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2
    """ for simplicity, we will only consider positive numbers
    """
    return n if n > 1 else 0.5
```
The function first checks if the input number is greater than 1. If it is, it returns 0.5. If the number is not, it returns the integer part of the number, which is the largest integer that is less than the given number.