```python
def unique(l: list):
    return list(set(l))

# Test the function with various inputs
assert(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])

# Test again with list of strings
assert(unique(["a", "e", "you"]) == ["a", "e", "you"])
```
This code provides a function unique that returns a list containing only the unique elements from the input list. The test cases ensure thening that the function behaves as expected.