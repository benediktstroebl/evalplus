```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float("inf")]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

I hope this helps you with your problem! Please let me know if I can assist you with any other way!