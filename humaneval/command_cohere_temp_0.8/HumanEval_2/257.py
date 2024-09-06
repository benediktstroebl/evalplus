```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to return the decimal part of the input number. This is achieved by subtracting the closest integer (rounded down) from the input number. This integer part represents the largest integer that is less than or equal to the input number, and the remainder becomes the decimal part, which is always less than or equal to 1. The function then returns this decimal part, providing a convenient way to access only the decimal portion of the input number.