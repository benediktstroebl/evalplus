```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The Python script provided defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive elements from the original list. This function implements the filtering process through a list comprehension that checks each element in the list against the condition `x > 0`, which selects only the elements that satisfy this condition.