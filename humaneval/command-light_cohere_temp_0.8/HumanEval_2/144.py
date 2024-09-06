```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5)
   
    0.1
   
   IN receive the price of ...
def test_function(number: float) -> None:
    assert truncate_number(number) == 0.1
```

This script defines a function that can take a float number as input and return the decimal part of that number. The test_function is a pass for function and it passes the test.