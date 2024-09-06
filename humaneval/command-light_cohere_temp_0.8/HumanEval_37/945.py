```python
def sort_even(lst):
    """Sorts even numbers in a list, returning a new list."""
    return sorted([x for x in lst if x % 2 == 0], key=lambda x: x)

# Test code
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```