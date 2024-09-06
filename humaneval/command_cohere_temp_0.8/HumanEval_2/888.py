```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, leaving behind the residual fraction. 

To test this, try calling the function with the input `7.5` and observing that the output is `0.5`.