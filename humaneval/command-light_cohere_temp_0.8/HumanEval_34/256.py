```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float("inf")]

# Test case 1:
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2:
test_case2 = [float("inf")]
assert unique(test_case2) == []

# Test case 3:
test_case3 = [1, 2, 3]
assert unique(test_case3) == [1, 2, 3]

print("All tests passed!")
```