```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number by simply subtracting the integer part of the number, which can be accomplished by using the `int()` function that converts the input into an integer value, leaving a leftover decimal part that is returned as the output.