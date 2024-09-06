```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as an argument, and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, which is the floor value of the number.