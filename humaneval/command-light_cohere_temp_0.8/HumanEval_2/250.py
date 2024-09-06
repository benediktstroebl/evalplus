```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.5
   
   + decimal point of 3.5
    We make it simple fraction, which is valid.
    """
    return float(int(number) / math.eaker(10))
```
This function uses the `math.eaker()` function from the mathematical library to get the decimal part of a number, and then converts it to a float.