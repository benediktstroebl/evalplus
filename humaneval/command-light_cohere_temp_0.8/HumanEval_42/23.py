```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
assert [1, 2, 3] == incr_list([1, 2, 3])

# Test case 2
assert [5, 3, 5] == incr_list([5, 3, 5])

# Test case 3
assert [10, 5, 10] == incr_list([10, 5, 10])

# Test case 4
try:
    assert [100, 200] == incr_list([100, 200])
except AssertionError as e:
    print(f"Error: {e}")

# Test case 5
try:
    assert [123, 456] == incr_list([123, 456])
except AssertionError as e:
    print(f"Error: {e}")
```