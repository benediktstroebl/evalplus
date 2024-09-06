```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and x not in [-None, float('inf')] and seen.add(x)]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```