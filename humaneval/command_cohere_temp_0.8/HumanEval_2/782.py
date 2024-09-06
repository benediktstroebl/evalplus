```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, leaving behind the residual fraction. 

To test this, try calling the function with the input `3.5` and observing the return value of `0.5`. 

This approach leverages the fact that floating point numbers can be decomposed into an integer part and a fractional part. By subtracting the integer part (the largest integer less than the number), the fractional part is isolated and returned.