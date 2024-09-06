```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part of the decomposition), hence leaving only the leftover fraction, i.e., the decimal part of the initial number.