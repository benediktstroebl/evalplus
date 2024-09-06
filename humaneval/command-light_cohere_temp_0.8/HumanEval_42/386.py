```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [i+1 for i in l]
    assert len(l) == n + 1, f"Unexpected list length: {l}"
    return l

# Example usage
lst1 = [1, 2, 3]
incr_list(lst1)
assert lst1 == [2, 3, 4]

# Test if the function modifies the original list
lst2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
lst3 = lst2[:]  # Create a copy
incr_list(lst3)
assert lst3 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test with a list of strings
lst4 = ["hello", "world"]
incr_list(lst4)
assert lst4 == ["hello", "world", "ow!", "lrdd"]
```