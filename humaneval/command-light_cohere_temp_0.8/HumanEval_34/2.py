```python
def unique(lst):
    return list(set(lst))

def test_unique(lst):
    assert unique(lst) == [0, 2, 3, 5, 9, 123]

print("Unique function works!")
```