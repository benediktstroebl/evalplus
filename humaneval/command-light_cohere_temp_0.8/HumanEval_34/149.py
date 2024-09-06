```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

The function unique uses the set() function to remove duplicates from the input list and then converts it back to a list. In the test_unique function, we pass the test_unique function test suite to ensure the unique function works correctly.