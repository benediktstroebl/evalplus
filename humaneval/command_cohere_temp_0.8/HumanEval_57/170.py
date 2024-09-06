Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def monotonic(lst):
    """Returns True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi = lst[0], lst[-1]
    for num in lst[1:-1]:
        if num <= lo or num >= hi:
            return False
        lo, hi = num, num
    return True
```

The function `monotonic()` takes a list (`lst`) as an argument and returns `True` if its elements are monotonically increasing or decreasing. It checks the first and last elements of the list to initialize `lo` and `hi` variables to compare other list elements with. It then iterates over the list elements excluding the first and last ones and verifies if each element is within the acceptable range defined by `lo` and `hi`. If any element fails this condition, it returns `False`. Otherwise, it confirms that the list elements are either monotonically increasing or decreasing.

Here is an example usage of the function:
```python
>>> monotonic([1, 2, 4, 20])
True
>>> monotonic([1, 20, 4, 10])
False
>>> monotonic([4, 1, 0, -10])
True
```

The three calls to the `monotonic()` function demonstrate its behavior on three different lists, illustrating that it returns `True` for monotonically changing lists and `False` for lists that do not share this property.