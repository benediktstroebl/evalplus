```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part of the decomposition described in the prompt). The resulting difference will be the residual decimal part of the initial number. 

Here is a test case to confirm the correct functionality of the function:
```python
assert truncate_number(3.5) == 0.5
```