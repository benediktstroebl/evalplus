```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the initial number given, as the residual will be the decimal part desired. 

To test this script, you can call the function with the input `3.5` and compare the output to `0.5`.