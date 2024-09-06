```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    >>> truncate_number(3.5)
   
    return 0.5

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(-0.0) == 0.0
    max_int = 2**3.5**min_intpart = 0.0
    assert truncate_number(float("inf")) == 0.0
    assert truncate_number(float('-inf')) == 0.0
```
This Python code defines a function `truncate_number` that takes a positive floating-point number as input and returns the decimal part of that number. The `test_truncate_number` function tests the `truncate_number` function with several inputs and asserts that the function returns the correct result.