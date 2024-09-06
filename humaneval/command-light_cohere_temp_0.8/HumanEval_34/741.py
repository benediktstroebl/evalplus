```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test case 1: Should return list with 4 unique elements [0, 2, 3, 5]
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0])
assert len(test_unique) == 4, "Should return 4 unique elements"

# Test case 2: List has more than one unique element
test_unique = unique([5, 3, 5, 2, 3, 9, 0, 123])
assert len(test_unique) > 1, "Should have more than one unique element"

# Test case 3: Should handle empty list correctly
test_empty = unique([])
assert len(test_empty) == 0, "Should return an empty list"
```