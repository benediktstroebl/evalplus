```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> test = truncate_number(3.5)
    
    assert test == 0.5 
    assert test > test
   
    assert test >= 0.25 
    assert abs(test - 1.0) <= 1e
```

This function takes a number as an argument and returns the decimal part of that number. It can be used to test if the function satisfies the stated requirements.