```python
def sort_even(lst):
    return lst[:][:]:

# Tests
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

test_sort_even()
```