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
This calls the function with the argument 3.5, and the returned value should be 0.5. 

This approach is by definition the simplest way to obtain the residual, as the definition outlined that the function need only return the 'leftover part always smaller than 1'. 

Please let me know if you'd like me to test this function with any other values or provide additional functionality.