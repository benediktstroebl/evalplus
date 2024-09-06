```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this function, you can call it with a float input like so: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This call will return 0.5, which is the decimal part of the original number 3.5. 

This function will return the correct decimal value for any valid input, as it is tailored to the specific problem statement.