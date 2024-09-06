```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    0.5
    
    Test a+ floating point numbers with decimals are
    one of the most common use cases, and Python has a function
    that can directly return the decimal part of such numbers.
    - It_to_float(string_number)

    Examples:
    >>> truncate_number(3.5)  #.0
    < the way for the simple example, it is the same as the previous
    function that you provided. 
```