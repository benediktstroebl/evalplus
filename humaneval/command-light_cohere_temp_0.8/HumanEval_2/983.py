```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = n // (n.value <= 1)
   
    decimal = n % (n.value)
   
    assert integer > 0,
    assert decimal <= 0.0,
    return decimal
return 0.5
```