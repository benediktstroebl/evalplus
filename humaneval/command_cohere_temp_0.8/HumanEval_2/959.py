```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals left in the difference will be less than 1, representing the desired decimal part of the number.