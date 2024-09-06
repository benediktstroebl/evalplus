```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function employs a set data structure, named 'seen', to efficiently track unique elements. It iterates through the input list 'l', checking each element. When it encounters an element that is not in the 'seen' set, it adds it through the set's add method (or ignores it if it's already present). The result list is created by selecting elements that successfully pass this test. To ensure consistency, the function then sorts the result list alphabetically. 

This approach delivers both efficiency and accuracy, making it a robust solution for the problem.