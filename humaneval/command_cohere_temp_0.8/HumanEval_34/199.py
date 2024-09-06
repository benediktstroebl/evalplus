```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This function utilizes a set, `seen`, to efficiently track unique elements. It iterates through the input list, checking if each element is already in the set. If it's not, the element is added to the set and included in the `result` list. The final output is a sorted version of this list, ensuring that the order of unique elements is sorted. 

The implementation is both effective in terms of performance and clarity of understanding, making it a strong solution to the problem. 

You may test this code by calling the function with a list of your choice, and it will return the sorted unique elements of that list, accordingly.