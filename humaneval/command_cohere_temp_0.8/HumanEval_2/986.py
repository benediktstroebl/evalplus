```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float number to an integer (using int function) and subtract the result from the original number, thus returning the fractional part (the decimal part) of the number. 

To test this function, you can call it with a float number, and compare the result with the original number to verify that the fractional part is correctly returned. 

Example:
```python
 truncate_number(3.5)
# Should return 0.5
``` 
This function can also be tested against the example provided in the problem statement, by comparing the results returned when the function is called with 3.5, as follows: 
```python
truncate_number(3.5) == 0.5
# Should return True
``` 
This should return **True** indicating that the function correctly returns the decimal part of the number.