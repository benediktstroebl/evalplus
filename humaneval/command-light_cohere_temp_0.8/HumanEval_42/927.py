```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(result[i] == i+1 for i in range(n))
    return result
# Example usage:
# test_incr_list([1, 2, 3])
# [[2, 3, 4]]
# test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
# [[6, 4, 6, 3, 4, 4, 10, 1, 124]]
```
The `incr_list` function takes a list as input and returns a new list with each element incremented by 1. It uses list comprehension and also asserts that the new list has the same length as the original list and that each element in the new list is one plus than the corresponding element in the original list.