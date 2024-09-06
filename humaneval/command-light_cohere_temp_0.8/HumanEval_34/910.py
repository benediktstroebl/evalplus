```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test case 1: Return unique elements from a list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
assert result1 == [0, 2, 3, 5, 9, 123]

# Test case 2: Return unique elements from an empty list
test_case2 = []
result2 = unique(test_case2)
assert result2 == []

# Test case 3: Return unique elements from a list containing duplicates
test_case3 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result3 = unique(test_case3)
assert result3 == [0, 2, 3, 5, 9, 123]

print("All tests passed!")
```