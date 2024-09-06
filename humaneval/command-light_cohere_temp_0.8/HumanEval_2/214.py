```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    >>> truncate_number(3.5)
    0.5
   
    EXCEPTION CAUGES 
    
    """
    assert number > 0 and number % 1 == 0, 
    assert abs(number - int(number)) < 0.5,
    return number - decimal


This function takes a number as input, and returns the decimal part of the number. It is written in a way that can be easily reused and tested for future use.