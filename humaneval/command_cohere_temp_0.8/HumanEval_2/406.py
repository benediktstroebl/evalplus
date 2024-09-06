```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the residual fraction.