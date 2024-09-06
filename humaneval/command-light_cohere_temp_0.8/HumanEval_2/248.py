```python
def truncate_number(number: float) -> float:
    return 0.1 if number >= 1 else number
```

The function tests if the number is less than 1, and if it is, returns 0.1. If the number is greater than then it returns number directly.