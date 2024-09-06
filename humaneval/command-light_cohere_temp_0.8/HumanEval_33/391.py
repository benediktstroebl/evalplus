```python
def sort_third(lst):
    """Sorts the list l such that values at indices divisible by three are in their correct positions."""
    return lst[:[lambda x: x % 3 == 0]][sort()] [3:] + [0] + lst[::-1][3:]

# Test
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
test_sort_third()
```