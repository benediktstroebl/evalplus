Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    return (lst[1:] + lst[:-1]) == sorted(lst)

# Tests
assert monotonic([1, 2, 4, 20])
assert not monotonic([1, 20, 4, 10])
assert monotonic([4, 1, 0, -10])
assert not monotonic([10, 5, 7, 3])
```

The `monotonic` function checks if the list is either monotonically increasing or decreasing. It uses a clever trick of adding and removing elements from the list to check if it's equal to a sorted version of the same list.