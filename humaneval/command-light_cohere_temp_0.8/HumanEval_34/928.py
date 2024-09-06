```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [17, 34, 67, 5, 18, 76]
assert unique(test_case2) == [17, 18, 34, 67, 76]

# Test case 3 (list of strings)
test_case3 = ["hello", "world"]
assert unique(test_case3) == ["hello", "world"]

# Test case 4 (empty list)
test_case4 = []
assert unique(test_case4) == []

# Test case 5 (single element list)
test_case5 = [17]
assert unique(test_case5) == [17]
```

This script defines a `unique` function that takes a list as an argument and returns a new list containing the unique elements from that list. The test cases demonstrate the approach by creating test lists and comparing the results with the expected output.