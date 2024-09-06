```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float number to an integer (using int function), and subtracts the result from the original number - this effectively slices off the integer part of the float number, leaving only the decimal part. 
For example:
```python
truncate_number(3.5)  # Returns 0.5
```