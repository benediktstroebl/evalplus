```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently removes the largest integer part and leaves behind the residual fractional part of the original number, which is necessarily less than 1.