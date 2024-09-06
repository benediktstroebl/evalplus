```python
def truncate_number(n):
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Returns: decimal part of the number.
        >>> print(truncate_number(3.5))
        0.41999)  #
```
This Python script defines a function called `truncate_number` that takes a single argument `n`. This function is designed to return the decimal part of the input number `n`, which is the largest integer smaller than `n` that can be represented as a decimal. The function uses the string formatting to return the part of the number as a string, with the decimal point representation of the integer part and the decimal part separated by a period.