```python
def median(lst):
    if len(lst) == 0:
        return None  # Handle empty list
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return (lst[mid] + lst[len(lst) - 1 - mid]) / 2
    else:
        return lst[len(lst) // 2]

# Unit tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 3.0
assert median([9, 8, 7, 6]) == 7
```