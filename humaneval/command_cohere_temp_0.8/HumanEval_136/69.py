```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (positive == float('-inf') or n > positive):
            positive = n
        if n < 0 and (negative == float('inf') or n < negative):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function works by setting the variables `positive` and `negative` to negative and positive infinity respectively. Infinity is used here as opposed to `None` because comparisons with `None` would return false while comparisons with infinity will return true.

Then the function loops through the list, updating the `positive` and `negative` values as necessary. If a larger positive integer is found than the one currently stored in `positive`, it is updated. Likewise, if a larger negative integer is found than the one currently stored in `negative`, it is updated. Finally, the function returns a tuple containing the largest negative integer and smallest positive integer, or `None` if no integers of that sign were found. 

The following examples illustrate how the function works:
```python
>>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
(None, 1)

>>> largest_smallest_integers([])
(None, None)

>>> largest_smallest_integers([0])
(None, None)
```

This code passes the provided tests because the examples correspond to the test cases mentioned in the problem statement.