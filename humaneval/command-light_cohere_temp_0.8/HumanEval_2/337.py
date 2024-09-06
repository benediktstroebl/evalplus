```python
def truncate_number(number: float) -> float:
    return round(number) // 1 if number > 1 else number
```
This code defines a function called `truncate_number` that takes a float number as an argument and returns the decimal part of the number, which is the integer part divided by 1. The function uses the floor division to remove the fractional part and only return the integer part. It uses the simple boolean condition to determine if the number is greater than 1, and in that case, it returns the floor division of the number. In case the number is equal to or less than 1, it simply returns the number as it is, without any modifications.