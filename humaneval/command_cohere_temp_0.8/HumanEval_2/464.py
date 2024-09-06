```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number`, which is the floor of the number from `number` to achieve the desired result.