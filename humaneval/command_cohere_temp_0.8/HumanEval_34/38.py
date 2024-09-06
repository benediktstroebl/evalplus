```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called `unique` that takes a list `l` as an argument. It employs the set method to eliminate duplicate entries from the list, ensuring that each element appears only once. Subsequently, the sorted() function is used to organize these unique elements in ascending order. The function then returns the sorted unique list.

This solution offers a concise and efficient method to handle the task of retrieving unique elements from a list while maintaining their order.