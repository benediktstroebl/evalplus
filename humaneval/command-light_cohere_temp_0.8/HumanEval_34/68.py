```python
def unique(lst):
    return sorted((item for item in lst if item not in set(lst)))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [1, 2, 2, 3, 4, 5]
assert set(unique(test_case2)) == set([1, 2, 3, 4, 5])

# Test case 3
test_case3 = [a, b, c]
assert unique(test_case3) == [a, b, c]
```
This script defines a function `unique` that returns a list containing unique elements from an input list, where an element is considered unique if it is not present in the set of all elements in the original list. The test cases demonstrate the roll out the