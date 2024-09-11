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

This script does the following:
1.  It defines a function `unique(l: list)` that takes a list `l` as input.
2.  Inside the function, `set(l)` is used to remove duplicates from the list. This is because sets in Python cannot contain duplicate elements.
3.  The `sorted` function is used to sort the unique elements in ascending order.
4.  The function is then tested with a list of numbers to demonstrate its usage.

When you run this script, it will print the unique elements from the list in sorted order.