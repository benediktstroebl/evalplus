```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.1
   
    big enough to not fit in this range, will return 0.0.  """ 
    >>> truncate_number(-3.5) == -0.1
    particular test
    TDD case, negative numbers are also valid inputs
    """

    return number / (10**(math.ceil(number))  # Remove the decimal part and return as a floating point number

# Test cases
assert truncate_number(3.5) == 0.1
assert truncate_number(-3.5) == 0.1
assert truncate_number(10**6) == 1.0
assert truncate_number(10**(7)) == 1.1
assert truncate_number("1000.0") == 1.0
assert truncate_number(123.456) == 1.456
assert truncate_number("abc123") == 1.123

Do you need assistance with anything else?