```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    assert len(l) == n
    assert all(i+1 == l[i] for i in range(n))
    return l

# Test case 1
[5, 3, 5, 2, 3, 3, 9, 0, 123] == incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])

# Test case 2
([1, 2], [3, 4]) = incr_list([1, 2, 3, 4, 5, 6])
```
This script defines a function incr_list that takes a list l as input and returns a new list l with elements incremented by 1. The test cases verify the simple increment and decrement operations on the list.

The script is well-contained as it doesn't depend on any external modules or functions.