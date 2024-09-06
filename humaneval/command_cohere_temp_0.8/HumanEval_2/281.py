```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply takes the parameter and subtracts the largest integer 
less than the parameter. 
The resulting value is the residual which always lies between 0 and 1 and 
is the decimal part of the number (with a possible 0 before the decimal point). 

It is the most straightforward way to do it and it completes the task in a 
test-worthy manner.

Here is an example of an invocation:
```python
truncate_number(3.5)
```

The resulting output will be:
0.5

This function has a straightforward implementation, and its usefulness 
can be observed in various numerical contexts.  It is also readily testable 
for any numeric value to validate its behavior against expectations.