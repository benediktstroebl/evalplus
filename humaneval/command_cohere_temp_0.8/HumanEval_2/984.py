```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals in the number will be subtracted, leaving only the integer part. 

To test this, try calling the function as follows:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
The resulting output of 0.5 would indicate that the function is working as intended.