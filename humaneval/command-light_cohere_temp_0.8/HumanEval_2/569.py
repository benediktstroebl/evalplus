```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    object
 smaller numbers, the integer part will be bigger than the decimal part.
    >>> truncate_number(0.1) == 0
   0
    larger numbers, the integer part will be smaller than the decimal part.
    """
    number = float(input())
    ans = number // int(number)
    return ans
```