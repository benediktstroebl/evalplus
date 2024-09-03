```python
def add(lst):
    """Given a non-empty list of integers lst. add(i) such results at odd indices
    Examples:
        [4, 2, 6, 7] ==> 2 
    """
    assert len(lst) > 0
    assert all(isinstance(i, int) for i in lst)
    assert all(i % 2 == 1 for i in lst)
    assert sum(lst) == sum(map(add, lst)))
```