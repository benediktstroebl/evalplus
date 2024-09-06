```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the residual decimal part of the original number.