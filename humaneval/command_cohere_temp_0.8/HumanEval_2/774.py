```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which gives the residual decimal part. 

Here is a simple test case to verify its behavior:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(8.0) == 0.0
```