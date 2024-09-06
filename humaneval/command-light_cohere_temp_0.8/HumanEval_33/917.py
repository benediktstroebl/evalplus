```python
def sort_third(l: list):
    """Sorts list l such that all values not divisible by three are moved last.
    l = [list()
    list of non-negative integers
    n = len(l)
    if n % 3 == 0:
        return l
    if n < 3:
        return l[:n//3] + [x for x in l[n//3:] + l[n%3:]][:n//3] + l[n:]
    else:
        return l[:n//3] + [x*(1+3) for x in l[n//3:] + l[n%3:]] + l[n:]

# Unit Tests
def test_sort_third():
    list_values = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    got = sort_third(list_values)
    assert got == expected
```