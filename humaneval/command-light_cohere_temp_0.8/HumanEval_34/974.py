```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [0, 2, 3, 5, 9, 123]
    assert unique(lst) == expected

if __name__ == "__main__":
    test_unique()
```
The function unique takes a list as an argument and returns a new list containing only the unique elements from the original list. This is using the's set() and sorted() functions to ensure that all unique elements are returned in sorted order.