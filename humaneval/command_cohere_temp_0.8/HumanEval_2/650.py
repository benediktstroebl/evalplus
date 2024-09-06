```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as an argument, and returns the decimal part of the number. It does so by taking the difference between the original number and the largest integer less than or equal to the number, which can be achieved by converting the number to an integer using `int()`. The result is the residual decimal portion of the original number, providing the desired output.