```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function called `get_positive` that takes a list `l` as input. Within the function, it uses a list comprehension to iterate over each element `x` in the input list `l`. For each element `x`, it checks if `x` is greater than zero (`x > 0`). If this condition is true, the element `x` is included in the list that is returned by the function. If the condition is false, the element `x` is skipped, and nothing is added to the returning list. Ultimately, this function returns a new list that contains only the positive elements from the input list, regardless of the list's content and the types of the elements.