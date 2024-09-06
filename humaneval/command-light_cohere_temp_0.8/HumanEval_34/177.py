```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [0]]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

This code provides a function `unique` which accepts a list and returns a new list with unique elements. The function utilizes the sources elements from the list and utilizes a set to track seen elements. The function then iterates over the unique elements and adds them to the list if the element is not in the set. This process effectively filters out duplicate elements from the input list.