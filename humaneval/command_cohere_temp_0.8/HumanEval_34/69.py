```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements within l. Here's a breakdown of how it works:
1. The input list l is converted into a set using the set() function. This removes any duplicate elements from the set, ensuring that only unique elements remain.
2. The content of the set is then converted back into a list using the list() function. This may seem counterintuitive after removing duplicates, but this step is necessary to apply the sorting operation.
3. The resulting list of unique elements is sorted in ascending order using the sort() method.

Therefore, the function unique(l) will return a new list containing sorted and unique elements from the input list l. For example, unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) will return [0, 2, 3, 5, 9, 123].