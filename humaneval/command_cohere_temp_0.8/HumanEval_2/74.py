```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently truncates the number to the decimal part alone, which is the desired result. 

To test this function, you can call it with a floating point number as follows: 
```python
truncate_number(3.5) 
# Output: 0.5
```
The resulting output of 0.5 demonstrates that the function correctly returns the decimal part of the input number.