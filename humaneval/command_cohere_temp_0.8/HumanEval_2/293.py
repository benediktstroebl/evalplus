```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, as expressed by the expression `int(number)`. This effectively extracts the integer part of the number and discards it, leaving only the decimal part. 

Here are some example outcomes of the function:
```
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
>>> truncate_number(10.99)
0.99
``` 

This method offers a straightforward and efficient way to isolate the decimal part of a floating-point number.