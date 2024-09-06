```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, as the remaining value will be the decimal part. 

To test this function, execute it with different parameters to observe the output. For example:
```python
print(truncate_number(3.5)) # Should print 0.5
print(truncate_number(12.345)) # Should print 0.345
print(truncate_number(0.5)) # Should print 0.0
``` 
This will help ensure the function works as intended.