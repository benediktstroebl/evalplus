```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, leaving behind the residual fractional part. 

To test this function, you can call it with a few numeric values:
```python
truncate_number(3.5)
# Expected output: 0.5

truncate_number(12.345)
# Expected output: 0.345

truncate_number(111.222)
# Expected output: 0.222
```
If you want to test edge cases, try values such as `1.5`, `2.5`, or `3.0` to confirm that the function correctly identifies the truncation point to be at the nearest integer less than or equal to the input value.