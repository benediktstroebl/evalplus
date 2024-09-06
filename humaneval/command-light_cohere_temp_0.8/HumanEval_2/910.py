Here's the solution:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number.

    >>> return 0.5 * number if integer part + division,
    """

This function takes a number as input and returns the decimal part of that number, which is the leftover part after dividing the number by 10. 

The function uses the division to get the integer part of the number, and then returns the decimal part of the number, which is always smaller than 1. 

This function can be used to solve the problem of truncating a positive floating point number to a decimal number that is always smaller than 1.