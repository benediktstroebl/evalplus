```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the number, which is achieved by converting the floating point number to an integer using `int()`, effectively cutting off the integer part of the number and leaving behind the desired decimal part.