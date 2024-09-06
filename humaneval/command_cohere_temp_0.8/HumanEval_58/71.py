```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` and returns the sorted unique elements that are present in both lists. This is done using the `set` data type in Python, which automatically removes duplicate elements. The `intersection` method returns a set of the elements that are present in both `l1` and `l2`. Finally, the result is sorted to ensure consistent ordering of elements. 

This approach ensures that each element is unique in the output and that common elements are preserved and collected from both lists.