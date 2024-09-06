```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which inherently removes the largest integer part and leaves behind the residual fraction. 

To test this, try invoking the function with the following values:
```python
truncate_number(3.5)  # Expected: 0.5
truncate_number(8.0)  # Expected: 0.0
truncate_number(11.2) # Expected: 0.2
```
The expected output should confirm the correct operation of the function.