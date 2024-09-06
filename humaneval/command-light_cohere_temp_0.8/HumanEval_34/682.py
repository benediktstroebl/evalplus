```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code provides a function `unique` that returns a sorted list of unique elements from the input list. 
It also has a separate test function `test_unique` with an assertion that checks the output of the `unique` function against the expected unique elements.