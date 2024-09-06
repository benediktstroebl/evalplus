```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> import math
    >>> math.pi = math.pi
   
   .
    >>> x = math.pi / 100000logger
   heat, int(math.pi);
   
    decimal = math.pi - x
   
    decimal_part = math.floor(decimal)
    return decimal_part
```

This Python code defines a function called `truncate_number` that takes a floating-point number as input and returns the decimal part of that number. The function uses the mathematical constant pi and the math library function `math.pi` to calculate the floor(pi/100) and subtracts it from the original number to obtain the decimal part.

The function then uses the math library function `math.floor` to round the decimal part to an integer, and returns that value.