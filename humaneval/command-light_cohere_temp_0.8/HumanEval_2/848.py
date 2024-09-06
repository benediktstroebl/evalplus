```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> test = truncate_number(10.0)
    result = 0.1
    print("test:", test) 
    assert test == 0.1
   
    result = truncate_number(10.5)
    print("result:", result)
    assert result == 0.1 
    assert result < 10.0 
    assert result <= 1.0 
    assert result >= -1.0 
 print("Passes all tests!")
```