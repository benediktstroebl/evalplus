```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function called unique which takes a list l as input. Inside the function, it uses a set seen to keep track of unique elements encountered while iterating through the input list. It utilizes a list comprehension to filter elements that are not already in the seen set and adds them to the result list. Finally, the function returns a sorted version of the result list, containing the sorted unique elements from the input list.