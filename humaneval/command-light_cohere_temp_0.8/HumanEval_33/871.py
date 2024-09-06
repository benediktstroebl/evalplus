```python
def sort_third(l: list):
    """Sorts list l so that values not divisible by three remain in their original position, while values divisible by three are sorted to the rear."""
    return [x for x in l if x % 3 != 0] + [x for x in l if x % 3 == 0]

# Test
def test_sort_third():
    l = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    actual = sort_third(l)
    assert actual == expected
```