```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function `unique` that takes a list `l` as an argument and returns a new list with unique elements from the original list, using the `set()` function to remove duplicates and the `list()` function to convert it to a list. By passing the unique function with a test_unique function, the code verifies that the unique function works correctly and returns the expected unique elements in the list.