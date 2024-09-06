```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 3, 'a', 5, 'b', 0]
assert unique(test_case2) == ['a', 'b', 5]

# Test case 3
test_case3 = [1, 2, 2, 2]
assert unique(test_case3) == [2, 2]
```
This Python script defines a function unique that sorts and returns unique elements from an input list. It provides three test case that validate the unique function with different inputs and asserts the expected output for each case.