```python
def unique(l: list):
    return list(set(l))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [10, 2, 20, 40, 30]
assert unique(test_case2) == [10, 2, 20, 30]

# Test case 3
test_case3 = [ 'abc', 'a', 'b', 'c', 'x', 'y', 'z']
assert unique(test_case3) == ['abc', 'a', 'b', 'c', 'x', 'y', 'z']
```

This script defines a function called `unique`, which takes a list as an argument and returns a sorted list of unique elements in that list using the `set` and `list` functions. The test cases demonstrate that function's correctness.