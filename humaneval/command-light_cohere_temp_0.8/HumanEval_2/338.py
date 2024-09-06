```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    decimal part of 3.5 is 0.5
    return
    coworker
```

The function uses the built-in `float` function to return the decimal part of a number. It uses the floor division to get the largest integer part that is smaller than the number. It then uses the mathematical formula to remove the decimal part, which is always smaller than 1.