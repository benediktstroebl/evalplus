```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not  == " " and item]

# Test cases
tests = [
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], "should return"),
    ([], "should be empty"),
    ([4, 9, 2, 1], "order matters"),
    ([10, 20, 30], "returns sorted list"),
    ([7, 2, 3], "support non-integers"),
]

for test in tests:
    assert unique(test[0]) == test[1]
```