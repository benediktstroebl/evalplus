```python
def sort_third(l: list):
    """Sorts a list l so that values not divisible by three are at the beginning and the values divisible by three are at the end of the list"""
    l.split([i, j for i,j in l if i % 3 == 0 and j % 3 == 0])
    l[:-j] = l[j:][::-1]
    return l

def test_sort_third():
    """Function that tests the sort_third function"""
    lst = [1, 2, 3, 6, 3, 4, 8, 9, 2]
    assert list(sort_third(lst)) == [1, 2, 3, 6, 3, 4, 8, 9, 5]
```