```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` takes a single parameter, `number`, which is a positive floating point number. It returns the decimal part of the number by subtracting the integer part of the number from the input. The integer part of the number is obtained using the `int` function which returns the largest integer less than or equal to the given number. The remaining fraction is returned as the decimal part. 

This code assumes that the input is a positive floating point number which has an integer part less than or equal to the input number.