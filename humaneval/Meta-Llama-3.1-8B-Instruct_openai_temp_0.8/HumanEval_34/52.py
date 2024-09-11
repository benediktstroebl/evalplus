```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as an input, removes duplicates by converting it to a set, and then returns the sorted list of unique elements. The `sorted` function is used to sort the list in ascending order. The test case at the end demonstrates the function's usage. 

When you run this script, it will print the sorted list of unique elements from the test case: `[0, 2, 3, 5, 9, 123]`. 

Note that this function has a time complexity of O(n log n) due to the sorting, where n is the number of elements in the list. It also has a space complexity of O(n) because it creates a new set to remove duplicates. If the input list is large, this function may use a significant amount of memory.