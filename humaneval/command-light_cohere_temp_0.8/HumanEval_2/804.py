```python
def truncate_number(number: float) -> float:
    return (number // 1) * 1 if number > 1 else number
```

This Python code defines a function `truncate_number` that takes a floating point number as input and returns the decimal part of the number. The function uses a condition to check if the input number is greater than 1. If the input number is greater than 1, the function returns the decimal part by dividing the number by 1 and then multiplying the result by 1. Otherwise, the function returns the input number as it is.