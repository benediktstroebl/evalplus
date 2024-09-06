```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number, subtracts the closest integer to it (using int()), and returns the residual. This residual is the decimal part of the original number, which is the requested output. 
The function documentation is also included, as it is a requirement mentioned in the prompt.