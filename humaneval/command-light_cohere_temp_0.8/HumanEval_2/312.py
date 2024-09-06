```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.1
   
    practical test:
    - returns the decimal part of 3.5, which is less than decimal point
    - handles the leftover part by returning a number smaller than 1
    - tests for it working correctly
    """
    return 1 - math.floor(number)
```