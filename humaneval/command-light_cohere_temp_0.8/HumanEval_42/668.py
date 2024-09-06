```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [i+1 for i in range(n)] + l
    return res

# Test case 1: Basic incrementation
assert list(incr_list([1, 2, 3])) == [2, 3, 4]

# Test case 2: Existing element stays same
assert list(incr_list([5, 3, 5])) == [5, 3, 5]

# Test case 3: List with 0 and big number
assert list(incr_list([9, 0, 123])) == [10, 0, 124]

# Test case 4: New element added
assert list(incr_list([0, 123])) == [1, 123]

# Test case 5: Reversing incrementation
assert list(incr_list([1, 2, 3], -1)) == [1, 2, 3]
```