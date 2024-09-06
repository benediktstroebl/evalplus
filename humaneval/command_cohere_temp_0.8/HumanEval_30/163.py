```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list (`l`) as an input and returns a new list that contains only the positive elements of the original list. It uses a list comprehension to iterate over each element `x` in the input list `l` and checks if `x` is greater than zero. If `x` is greater than zero, it includes it in the resulting list.

The script doesn't include any additional dependencies or imports, making it self-contained and easier to use directly anywhere else.