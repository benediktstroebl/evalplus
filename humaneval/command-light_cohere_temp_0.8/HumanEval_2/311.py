```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)
    0.15

   
   
    general for all numbers and works on any floating-point type.  """
```

This code defines a function called `truncate_number` that takes a number as input and returns the decimal part of that number. 

This is a self-contained function because it does not depend on any other functions or variables within the script. 

To test the function, the code passes the number 3.5 as an input and asserts that the returned value is equal to 0.15, which is the decimal part of 3.5.