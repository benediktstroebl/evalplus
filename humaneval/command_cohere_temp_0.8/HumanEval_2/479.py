```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the initial number given, as the residual will be the decimal part desired. 

To test this script, you can call the function with the example provided in the problem statement:
```python
truncate_number(3.5)
# Expected output: 0.5
``` 
This will return 0.5, which is the decimal part of the number 3.5. 

This approach is intuitive and straightforward, providing a simple solution to the problem.