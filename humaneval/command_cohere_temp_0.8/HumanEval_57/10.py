Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = b = float(l[1])
    for x in l[1:]:
        if x <= a:
            return False
        if x > a:
            a = x
        if x >= b:
            return False
        b = x
    return True
```

This script defines a Python function called `monotonic` that takes a list `l` as input. The function returns `True` if the elements of the list are monotonically increasing or decreasing. It first checks if the list has at least two elements (`if len(l) <= 1:`) to ensure there are at least two elements to compare. It then uses two variables, `a` and `b`, to keep track of the smallest and largest elements seen so far. It then loops through the list, comparing each element `x` to the largest element seen `a` and the smallest element seen `b`. If `x` is smaller than `a`, it means the list is not increasing, and if `x` is larger than `b`, it means the list is not decreasing. Finally, if the loop completes without returning `False`, the list is either increasing or decreasing, and the function returns `True`. 

The function includes a simple unit test that verifies the correct behavior for three different examples:
```python
def test_monotonic():
    assert monotonic([1, 2, 4, 20])
    assert not monotonic([1, 20, 4, 10])
    assert monotonic([4, 1, 0, -10])
```

You can use this code to test the function with different input lists to see if it correctly identifies monotonically increasing or decreasing elements.  This approach has a time complexity of O(n), where n is the length of the input list.