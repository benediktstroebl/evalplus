```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer less than number from number, which is the same as appending 0 to the decimal part of the number, and thus removes the integer part while keeping the decimal part.