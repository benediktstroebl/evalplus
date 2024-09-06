```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    new_intpart = None
    new_decimals = []
    while abs(number) > 1:
        fraction = number
        number = float(1) - fraction
        new_intpart = int(number)
        new_decimals.append(fraction)
    new_decimal_part = (number - new_intpart)

    return new_decimal_part
```
This Python script defines a function `truncate_number` that converts a positive floating-point number into its decimal part. The function begins by establishing variables for the integer part and the remaining decimal part of the number. It then enters a while loop, which continues until the absolute value of the number exceeds 1. Inside the loop, it computes the decimal part by subtracting the fraction from the number, then computes the integer part by converting the number to an integer and extracting the integer part. Finally, the decimal part is returned, representing the decimal component of the original number.