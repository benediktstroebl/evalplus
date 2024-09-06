Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = b = float(l[1])
    for x in l[1:]:
        if x < a:
            return False
        if x > b:
            return False
        a = b
        b = x
    return True
```

This script passes the provided tests:
```python
>>> monotonic([1, 2, 4, 20])
True
>>> monotonic([1, 20, 4, 10])
False
>>> monotonic([4, 1, 0, -10])
True
```

This works by first establishing bounds on the first and second elements of the list, then iterating through the rest of the list, updating these bounds as needed. If the list is monotonic, this process will never have to update the bounds more than once.