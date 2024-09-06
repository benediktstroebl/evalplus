```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.2
   
   
   
    decimal part is 2.
    """
```

This code defines a function called `truncate_number` that takes a float number as an argument and returns the decimal part of that number. The function uses the positive floating point number as input and returns the decimal part of that number, which is always less than 1.