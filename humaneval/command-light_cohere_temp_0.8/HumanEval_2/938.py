```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.25
    requires python>=3.7 and is a 10 min since decimal digits, and is always equal to the integer part of the number. 

For instance, 3.5 has 10 decimal digits, and so the result will be 10. 
This function always returns a positive number, so you can ignore the negative sign when calling the function. 
This function can be useful in a variety of situations, such as working with large numbers or strings that represent numbers, or when you want to extract the decimal part of a number.