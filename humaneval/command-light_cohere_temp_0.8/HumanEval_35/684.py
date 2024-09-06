```python
def max_element(lst):
    if not_sorted(lst):
        return sorted(lst)[-max()]
    else:
        return lst[0]

# Unit Tests
def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

# Run the tests
test_max_element()
```

This script defines a function `max_element` that finds the maximum element in a list. It utilizes two strategies: one that uses the built-in `sorted` function and the maximum element of the sorted list, and the other one simply returns the first element of the list since it's the maximum. 

The script also provides a test function `test_max_element` that creates a test list and asserts that the `max_element` function returns the correct maximum element from the list.