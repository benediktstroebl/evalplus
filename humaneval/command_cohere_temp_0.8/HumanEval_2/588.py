```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (floor value). For example, `truncate_number(3.5)` returns `0.5`, as 3 is the largest integer less than 3.5 and the difference between them is 0.5.