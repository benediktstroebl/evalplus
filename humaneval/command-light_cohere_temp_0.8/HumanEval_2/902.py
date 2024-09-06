```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Parameters:
    number (float): Positive floating point number

    Returns:
    float: decimal part of the number
    """
    integer = number // 1
    decimal = number % 1
    return decimal
``` 
The function correctly decomposes the positive floating point number into its integer part and decimal part, and returns the decimal part of the number as the result.