```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)  #.3.5
   0
   Read
    need only float, decimal and integer parts of a number
    """

    # conversion to floating point number
    number = float(number)

    # removing the integer part
    decimal = number - round(number)

    # returning the decimal part of the number
    return decimal
```
This code defines a function called `truncate_number` that takes a single argument, `number`. It is designed to truncate a floating point number, extracting its decimal part. 

This function is efficient, self-contained, and straightforward, making it a concise and practical solution to the problem.