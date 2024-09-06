```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)
```

This function takes a positive floating point number as an input and returns the decimal part of the number. It does so by taking two integers, the number itself `number`, and the integer part of the number `int(number)`. The difference between these two constitutes the residual fractional part desired, as the `int()` function represents the largest integer less than or equal to the provided number. 

The function returns the decimal part of the number as the difference between the `number` and its closest integer value. 

To test this function, try calling it with a floating-point number and examining the output. 

For example:
```python
round(3.5) # 3
round(3.51) # 4
```
The first example outputs `3` versus `3.5` which has a decimal residual of `0.5`. The second example outputs `4` versus `3.51` which has a decimal residual of `0.01`. 

This function will work for any positive floating point number and will always return a value less than or equal to 1.0. 

To handle non-positive numbers, the function can be amended with a conditional check for `number > 0` before proceeding with the residual calculation.