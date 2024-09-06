```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test suite for function
def test_sort_even():
    l = [5, 6, 3, 4]
    assert sort_even(l) == [3, 6, 5, 4]
```