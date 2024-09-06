```python
def unique(lst):
    return list(set(lst))

# Test suite
tests = {
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123], "Should get unique elements"
    assert len(unique([5, 3, 5, 2, 3, 3, 9, 0])) == 6, "Should get the expected length"
    assert len(unique([1, 2, 3, 4, 5, 6]))) == 4, "Should handle duplicate elements"
}
```