```python
def sort_third(lst):
    """Returns a list l' such that all the values in l' are greater than the values in l, except those which are divisible by three. The values at the  corresponding positions in l and l' are equal, but the values are sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return lst[:] if any(x%3 == 0 for x in lst) else lst

# Add some test cases
test_sort_third = []
test_sort_third.append([5, [1, 2, 3], [5, 6, 3, 4, 8, 9, 2]])
test_sort_third.append([5, [1, 3, 4, 8, 9], [2, 6, 3, 4, 5, 8, 7]])
test_sort_third.append([1, [1, 2, 8, 9, 3, 4, 6], [3, 4, 5, 6, 7, 2]])
```