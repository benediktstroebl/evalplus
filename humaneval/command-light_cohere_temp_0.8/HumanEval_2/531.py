```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.5
   
    basic case, the integer part of a number is the largest integer 
    which is smaller than the number.
    This function works by finding the largest integer which is less than or equal to the number, 
    then taking the difference between the number and that integer.

To test the correctness of the function, there are some code blocks that call the function with a number of different values, and ensure that the return values of the function match the expected results.