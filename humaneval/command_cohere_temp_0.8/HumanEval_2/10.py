```python
def truncate_number(number):
    """ Returns the decimal part of the number """
    return number - int(number)
```

To test the function, it can be called with a floating point number as an argument, and the result is the decimal part of the number. For example:
```python
truncate_number(3.5)  # Returns 0.5
``` 

This function works by taking the floating-point number and subtracting the largest integer that is less than it, which is the integer part of the number. The result is the residual, which is the decimal part of the number. 

Would you like help with any other programming problems? Feel free to describe your request, and let's see if I can assist you in finding a solution!