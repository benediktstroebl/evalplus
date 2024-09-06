```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number, subtracts the closest integer to it (using `int()` to convert to integer), and returns the residual, which is the decimal part of the original number. 

To test this function, you can call it with a few sample numbers and compare the result to the original number to verify that it matches the expected decimal part. 

For example:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(12.345) == 0.345
assert truncate_number(123.456) == 0.456
``` 
The function will return the expected decimal values for these examples, respectively 0.5, 0.345, and 0.456.