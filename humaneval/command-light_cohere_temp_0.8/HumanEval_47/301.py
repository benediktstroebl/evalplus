```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[(length // 2) - 1]
# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([5, 5, 10, 10]) == 10
assert median([10, 10, 10, 10]) == 10
assert median([1, 2, 3]) == 2
assert median([-1, 2, 4]) == 1
assert median([5, 6, 7]) == 6
assert median([1, 2, 3, 4, 5]) != median([3, 1, 2, 4, 5])
```