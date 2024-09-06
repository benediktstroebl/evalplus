```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter into an integer and then returns the difference between the original number and the integer to get the decimal part of the number. 

To test this function, you can call it with a few different numerical values. Here's an example: 
```python
truncate_number(3.5)
# Expected output: 0.5

truncate_number(12.345)
# Expected output: 0.345

truncate_number(123.456)
# Expected output: 0.456
``` 

The function should return the decimal part of the number for all these tests. 

To execute the test, you can run the script or use the Python interpreter. The test cases will help verify if the function behaves as expected.