Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> truncate_number(3.5)
    0.5
   
    Support aed floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    """
    # Decompose the number into integer part and fractional part
    integer = int(n)
    fractional = n - integer
    # Return the fractional part
    return fractional
``` 

This function takes a positive floating point number as input and returns the decimal part of the number. It uses the decomposition method, where the number is represented as a sum of its integer part and fractional part.