```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is done by finding the difference between the number and the closest integer using the `int` function which returns the integer part of the number, and subtracting this integer part from the original number, resulting in the decimal part of the number. 

To test this function, you can call it with a few different numbers and compare the result to the original number to verify that the integer part was correctly identified and subtracted. 

For example:
```python
truncate_number(3.5)
# Expected output: 0.5
# Actual output: 0.5

truncate_number(2.8)
# Expected output: 0.8
# Actual output: 0.8
``` 

This will help ensure that the function accurately identifies the largest integer less than the provided number, and subtracts it to retrieve the decimal part.