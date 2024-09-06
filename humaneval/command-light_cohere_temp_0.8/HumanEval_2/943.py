```python
def truncate_number(number: float) -> float:
    return number // 10 if number >= 10 else number
```

This code defines a function `truncate_number` that takes a float number as input and returns the decimal part of the number. If the number is greater than 10, the function returns the floor division of the number divided by 10.