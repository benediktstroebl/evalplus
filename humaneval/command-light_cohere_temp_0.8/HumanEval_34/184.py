```python
def unique(lst):
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This Python code defines a function unique that returns a list of unique elements from an input list lst. The test_unique function tests the fact that the unique function correctly produces a list of unique elements from the input list [5, 3, 5, 2, 3, 3, 9, 0, 123].