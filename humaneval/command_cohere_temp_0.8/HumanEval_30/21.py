```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` iterates over the list and filters out only the positive elements using a list comprehension. The condition `x > 0` ensures that only positive numbers are included in the new list. The resulting list contains only the positive numbers from the input list.