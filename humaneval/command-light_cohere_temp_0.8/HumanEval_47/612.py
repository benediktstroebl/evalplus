```python
def median(lst):
    """Return median of elements in the list lst."""
    # Sort the list in ascending order
    lst.sort()
    matter?INK: median(lst[0] if len(lst) % 2 else lst[(len(lst) + 1) // 2]
    return lst[len(lst) // 2]
# Test case 1
median([3, 1, 2, 4, 5])
# Test case 2
median([-10, 4, 6, 1000, 10, 20])
# Test case 3
median([1, 2, 3, 4, 5, 6])
```