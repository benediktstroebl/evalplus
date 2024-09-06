```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1: basic incrementation
assert list(incr_list([1, 2, 3]) == [2, 3, 4])

# Test case 2: backward incrementation
assert list(incr_list([5, 3, 5, 2, 3, 3], -1)) == [5, 4, 5, 3, 3]

# Test case 3: empty list
assert list(incr_list([]) == [0])

# Test case 4: single element
assert list(incr_list([123])) == [124]
```
The code defines a function **incr_list** that takes a list l as input and returns a new list with elements incremented by 1. It uses list comprehension with a generator expression [i+1] to achieve this.

The test cases cover basic incrementation, backward incrementation, empty lists, and a single element.