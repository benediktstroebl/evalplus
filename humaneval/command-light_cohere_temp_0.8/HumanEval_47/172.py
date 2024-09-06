```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    
    if length % 2 == 1:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[(length // 2) + 1]

# Test the function
assert(median([3, 1, 2, 4, 5]) == 3.5)
assert(median([-10, 4, 6, 1000, 10, 20]) == 15.0)
```