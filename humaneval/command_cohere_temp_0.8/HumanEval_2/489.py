```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, and returns the decimal part of the number. The function simply subtracts the integer part of the number from the initial number provided, resulting in the decimal part, and returns it. 

To test this function, you can call it with a float, and compare the returned value with the expected value of the decimal part.