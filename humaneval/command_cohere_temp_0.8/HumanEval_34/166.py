```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements from l. Inside the function, a set seen is used to keep track of already-seen elements in the input list. The function then uses a list comprehension to iterate through the input list, checking if each element is already in the seen set. If it's not, the element is added to the set and included in the resulting list of unique elements. The list comprehension excludes elements that were already seen, ensuring that only unique elements are included in the output. Finally, the output is sorted using the sorted() function for a consistent order.