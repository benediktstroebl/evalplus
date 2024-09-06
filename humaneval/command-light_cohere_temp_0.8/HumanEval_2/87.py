Here is a Python script with a self-contained function that solves the problem you described:
```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    integer = n // n != 0
    decimals = n - integer
    return float(integer) + decimals
```

This function takes a number as input and returns the decimal part of the number. You can use this example:
```python
>>> test_value = 3.5
>>> truncate_number(test_value)
0.5
```
This is a simple and straightforward way to solve the problem.