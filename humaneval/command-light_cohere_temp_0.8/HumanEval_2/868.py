```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> import math
    number = float('3.5')
   
    do:
    number = math.floor(number)
    decimal = math.floor(number) - / math.floor(10.0)
    lost part = math.floor(10.0) - fraction = number - decimal - / math.floor(10.0)
    do:
    integer = math.floor(number)
    decimal = number - (fractional)
    integer = math.floor(decimal)
    decimal = (decimal * 10.0) + (fractional)
    decimal = str(decimal)
    return integer + decimal
```
This function takes a number as input and returns the integer part of the number. It does this by using the math module and performs floor division on the number. The integer part is then returned. The fractional part is returned as the decimal and integer are returned in a tuple.