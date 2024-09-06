```python
def median(lst):
    """Return the median of the list lst."""
    if len(lst) % 2 == 0:
        return (lst[(len(lst) // 2) - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]
# Test the function with various lists
test_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert median(test_lst) == 5.0
test_lst = [-10, 4, 6, 1000, 10, 20]
assert median(test_lst) == 15.0
test_lst = [5, 5, 5, 5]
assert median(test_lst) == 5.0
test_lst = [10, 20, 30, 40, 30, 10]
assert median(test_lst) == 25.0
```