```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list as an argument and returns a new list that contains only the positive elements of the original list. It uses a list comprehension to iterate over each element in the input list and checks if each element is greater than zero. If it is, the element is included in the resulting list.