```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.2 - number if number > 2
   2
    """

The code defines a function called `truncate_number` that takes a number as input and returns the decimal part of the number. The function uses an condition to return the decimal part of the number, which is the difference between the number and 2. The function then passes all test with the input 3.5, and returns 0.0 which is the the 3.5, the function will not return the expected decimal part (0.2). The difference desired number as a number.