```python
def truncate_number(number: float) -> float:
    return number // 10 if number >= 10 else number
```
The function takes a number as an argument, and returns the decimal part of that number. It checks if the number is greater than 10, and if it is, it returns the integer part of that number (the largest integer less than the given number) divided by 10. If the number is less than 10, it returns the original number as is.