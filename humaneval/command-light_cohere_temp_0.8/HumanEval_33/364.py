```python
def sort_third(l: list):
    """Sorts the list l such that values at indices divisible by three are sorted before non-divisible indices.
    l = list(range(l))
    l = [x for x in l if x%3 == 0]
    l.sort()
   ator(l)
    return l

def test_sort_third(test_list):
    test_list = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    got = sort_third(test_list)
    assert expected == got
```