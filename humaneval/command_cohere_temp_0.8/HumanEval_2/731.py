```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of the decimal part of a number. 

To test this function, you can call it with a few different floating point numbers and verify that the output is the expected decimal part of the number. 

For example:
```python
 truncate_number(3.5) == 0.5
truncate_number(2.8) == 0.8
truncate_number(5.0) == 0.0
```
All of these tests should pass.