```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    unique = set(l)
    return list(unique)

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123], "Error in test case 1"

# Test case 2
test_case2 = ['root', 'child', 'root']
assert unique(test_case2) == ['root', 'child'], "Error in test case 2"

# Test case 3
test_case3 = [0, 2, 3, 4, 5, 6, 7, 8, 9]
assert unique(test_case3) == [0, 2, 3, 4, 5, 6, 7, 8, 9], "Error in test case 3"

# Test case 4
test_case4 = [1, 2, 3, 4, 5, 6, 7]
assert unique(test_case4) == [1, 2, 3, 4, 5, 6, 7], "Error in test case 4"
```
The code defines a function `unique` that takes a list as input and returns a new list with unique elements from the original list, it uses the set data structure to keep elements unique and then converts it back to a list. In addition, the run four test cases to validate the `unique` function with different input lists.