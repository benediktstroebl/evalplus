```python
def sort_even(l: list):
    return l[1::2:]

def test_sort_even():
    assert sort_even([1, 2, 3]) == [2, 3, 1]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```