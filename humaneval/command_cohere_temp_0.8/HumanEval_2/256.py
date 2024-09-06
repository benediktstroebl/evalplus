```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of the decimal part of a number. 

To test this function, you can call it with a floating point input like so:
```python
truncate_number(3.5)  # Expected output: 0.5
```
The function's behavior on other examples of floating-point inputs can be verified in a similar manner. 
Please note that this solution is simplistic and does not take into account numerical precision or errors that might arise when dealing with extremely large or small numbers.