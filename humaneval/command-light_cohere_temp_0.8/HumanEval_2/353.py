```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    #Integer part
    integer = number // floor(number)
    return float(integer) + float('{:0.1f}8d of number')[:-1]
```

This code defines a function called `truncate_number` that takes a number as input and returns the decimal part of the number. This function is using the floor division to extract the integer part and then constructs the decimal part with the remainder of the division and the opening zeros. The decimal part is formatted as a string with 1 decimal place.