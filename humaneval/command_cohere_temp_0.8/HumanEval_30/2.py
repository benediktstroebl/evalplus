```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list (`l`) as an input and returns a new list that contains only the positive elements of the original list. The list comprehension uses the condition `x > 0` to filter out only the positive numbers from the input list.