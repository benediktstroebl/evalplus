Here's a Python function that solves the problem you described:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   0.5

``` 
The above code defines a function `truncate_number` that takes a float number as an argument and returns the decimal part of the number.