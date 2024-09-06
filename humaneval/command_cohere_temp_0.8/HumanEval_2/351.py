```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number by simply subtracting the integer part of the number, which can be accomplished by converting the number to an integer using `int()` and then subtracting this integer from the original number.