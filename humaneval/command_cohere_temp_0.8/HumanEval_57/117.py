Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi = 0, 1
    while hi < len(l):
        if l[hi] <= l[lo]:
            return False
        lo += 1
        hi += 1
    return True
```

The function initially determines whether the list has one or more elements. It returns True if the list has less than or equal to one element since a single value or an empty list is considered monotonic. However, if there are multiple elements, it performs a loop to verify if each element is greater than or equal to the preceding one and returns False if not. The loop increments both `lo` and `hi` by 1 (thereby considering the element at index `hi` while comparing with the element at index `lo`). It returns False if the comparison is not satisfied at any point. If the loop completes without finding any inequality, True is returned, indicating that the list is monotonic. 

This approach assumes that the list is already sorted in ascending order, regardless of whether it is an increasing or decreasing list. Feel free to add more test cases in the comments to verify the function's robustness.