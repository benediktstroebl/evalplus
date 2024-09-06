```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this function, you can call it with a floating point number argument, such as `truncate_number(3.5)`, which should return `0.5`.