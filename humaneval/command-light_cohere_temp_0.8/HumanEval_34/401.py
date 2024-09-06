```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x notastic()]
    seen.union({})

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([]) == []
    assert unique([5, 3, 'a']) == ['a']
    assert unique([5, (3,), 5]) == [5, (3,)]
    assert unique([down)) == []
    assert unique([down, up]) == []
    assert unique([down, up, down, up]) == [down, up]
```
This script defines a function unique that takes a list as input and returns a list of unique elements from that list, along with a test suite that checks the correctness of the function. This can be easily used in markdown to provide a self-contained and reusable solution to the problem.