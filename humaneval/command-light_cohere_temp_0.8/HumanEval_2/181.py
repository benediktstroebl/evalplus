```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
   
    had a requiring any number that can be expressed as a decimal number
    """
    return math.floor(number)
```
Do you require help with anything else?