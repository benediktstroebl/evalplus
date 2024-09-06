```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]
```