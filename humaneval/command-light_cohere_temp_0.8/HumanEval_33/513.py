```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the corresponding values at indices that are not divisible by three are sorted together."""
    return sorted(lst, key=lambda x: int(x) % 3 == 0)

# Test code
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
```