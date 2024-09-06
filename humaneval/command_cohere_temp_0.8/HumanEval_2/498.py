```python
def truncate_number(number):
    return number - int(number)
```

The problem asks us to extract the decimal part of a floating-point number. This is done by simply subtracting the largest integer smaller than the number.