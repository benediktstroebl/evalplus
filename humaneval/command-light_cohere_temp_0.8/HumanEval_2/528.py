```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.5
   
    flit
 total 0.5 = 0.5+ decimals and then part of 3.8 = 1
   
    remainder.5 of 1.0 and thest part has same 1, since the remainder is less than 1,
        so the decimal part is 0.5. 
    """Return 0.0 
    """unchan digits (print(0.5)
    decimal point of the number 3.5.
    """ print("Truncated value:", truncate_number(3.5))
    print("Decimal part:", round(truncate_number(3.5),1))
    """First test passes."""