```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the initial number given, as the residual will be the decimal part desired. 

To test this function, you can call it with a float input like so: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This call will return 0.5, as was stipulated in the original problem statement.