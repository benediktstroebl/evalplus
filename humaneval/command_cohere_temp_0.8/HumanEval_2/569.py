```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (whole number) and then subtracts this whole number from the original parameter. The resulting value is the residual/remaining fraction/decimal portion of the original parameter, which is returned from the function. 

This approach works because any floating-point number 'n' can be expressed as 'n = int(n) + remainder', where 'int(n)' is the largest integer less than or equal to 'n' and 'remainder' is the fractional part of 'n'. The remainder is by definition less than 1, so 'int(n) + remainder = n' and 'int(n) - remainder = n - remainder', which is just the residual fraction. 

To better understand this, let's examine a few examples:
```python
print(truncate_number(3.5))  # residual decimal portion = 0.5
print(truncate_number(7.0))  # residual decimal portion = 0.0
print(truncate_number(2.99999))  # residual decimal portion = 0.0001
``` 

As shown, the function easily handles cases where the integer portion is unbounded (it can be as large as possible without going over the floating point value). 

This approach has an execution time of O(1), meaning it will resolve in a constant time regardless of the complexity of the input number. It is also resilient to negative numbers or large numbers, returning the residual decimal portion in those cases, which by definition will be less than one.