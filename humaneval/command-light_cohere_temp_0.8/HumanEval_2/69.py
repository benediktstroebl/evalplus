```python
def truncate_number(n):
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    >>> truncate_number(3.5) 
    0.37500001e report: float(0.375) 

    # Test cases
    assert truncate_number(3.5) == 0.37500001
    Additionally THIS IS OK:
    assert truncate_number(0) == 0
    < 

This Python code defines a function called `truncate_number` that takes a single argument, `n`. It returns the decimal part of the number, which is the integer part of the number less than 1, divided by 1. The function uses the assert statement to test that the result is correct for a variety of input values, and the result is printed to the console.