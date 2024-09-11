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

In this script, the `unique` function uses the built-in `set` function to remove duplicates from the list, and the `sorted` function to sort the resulting list in ascending order. The test at the end prints the expected output for the provided example. 

This solution has a time complexity of O(n log n) due to the sorting, where n is the number of elements in the list. If you want to achieve this in O(n) time complexity, you can use a different approach with a dictionary or a set to remove duplicates, and then convert the resulting set back to a list. However, the `sorted` function is generally more efficient and easier to understand for small to medium-sized lists. 

Here is the alternative approach:

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    return sorted(x for x in l if not (x in seen or seen.add(x)))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this alternative solution, a set is used to keep track of the elements that have already been seen. The `x for x in l if not (x in seen or seen.add(x))` expression uses a generator to iterate over the list and add each element to the set only if it hasn't been seen before. This approach has a time complexity of O(n) because adding an element to a set is an O(1) operation on average.