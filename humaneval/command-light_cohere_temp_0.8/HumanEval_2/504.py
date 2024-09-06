```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.25

   0
   0.5
    simple test desired test theMAT test for a positive number, and returns the decimal part. 
    >> 
    Example test for a negative number:
    >>> truncate_number(-3.5) == 0.4
   0
   0.5
def test(number: float) -> bool:
    """
    Test if the number can be decomposed into a positive number 
    and a decimal part.
    >>> test(3.5)
   0.5
   
   0.20
   0.9
def test_number(number: float) -> float:
    """
    Given a floating point number, 
    return the decimal part of the number 
    >>> test_number(3.5)
   0.5
   0.1
   0.2
```
This script defines a function test_number, which tests if a given number can be decomposed into a positive number and a decimal part. The test returns True if successful, and False otherwise. It also defines a function, which returns the decimal part of a given number, given as a float parameter.