```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 0]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 3, 'abc', 5, 0, '123', 'abc', 'abc']
assert unique(test_case2) == ['abc', 5, 0, '123']

# Test case 3
test_case3 = [0, 2. serious, True, "hi"]
assert sorted(unique(test_case3)) == [0, 2, True, "hi"]
```

This script provides a function `unique` that takes a list as an argument and returns a new list containing only the unique elements from the original list. The test cases demonstrate how the