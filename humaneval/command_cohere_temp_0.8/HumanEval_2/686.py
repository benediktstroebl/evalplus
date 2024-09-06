```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number and returns the result. 

To test this, try calling the function with the input `3.5` and observing the output `0.5`. 

This approach utilizes Python's rounding down behavior in integer subtraction, which works due to the decimals being smaller than 1.