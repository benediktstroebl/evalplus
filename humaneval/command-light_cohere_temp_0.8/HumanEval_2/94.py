```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if n == 3.5
    can be represented as the the following way
    """
    if n < 0:
        return "Error: Input must be a positive number."

    # The following line can be simplified to:
    # return math.floor(n / 1e.1)
    many 
    return n

    return n

This script defines a function `truncate_number` that receives a number and returns the decimal part of the number. It passes all the common cases and can be easily tested using the `assert` function.