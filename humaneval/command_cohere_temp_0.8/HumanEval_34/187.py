```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called `unique` that takes a list `l` as input. It removes duplicate elements from the list using the `set()` function, which automatically eliminates duplicate values, and then sorts the unique elements using the `sort()` function. The sorted unique elements are returned as the result. 

The `unique` function ensures that duplicates are excluded and the elements are sorted in ascending order. 

To verify the functionality of the `unique` function, you can add a test case, like below, to confirm that it returns the expected result:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

Feel free to add more tests to cover different scenarios, such as lists with specific patterns of duplicates or nested lists.