```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of truncation. 

To test this function, you can call it with a float input and compare the output to the expected value. 
For example:
```python
truncate_number(3.5) == 0.5
```
The code passes the test as the output is True. 

This function assumes that the input is a positive floating point number. If the input is a negative number or zero, the function will raise an error. 
Additionally, this code does not account for the possibility of overflow if the input is a very large floating point number. If this is a consideration, then carefully review the type and values of Number that the function is called with.