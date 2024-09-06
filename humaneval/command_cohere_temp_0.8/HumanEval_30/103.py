```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that returns a list of positive numbers from an input list. It employs a list comprehension to iterate over each element in the input list (`l`). For each element `x`, it checks if `x` is greater than zero (`x > 0`). If the condition is true, the element is included in the resulting list that is returned. If the condition is false, the element is skipped, and nothing is returned for that iteration. In essence, this function efficiently isolates and returns a list containing only positive numbers from the input list.