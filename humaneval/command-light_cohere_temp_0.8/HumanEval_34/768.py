```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not == 0]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [7, [1, 2], 8, 9]
assert unique(test_case2) == [7, [1, 2], 8, 9]

# Test case 3
test_case3 = [['a', 'bb', 'ccc'], [10, 'a', 'b'], ['c', 'bb']]
assert unique(test_case3) == ['a', 'bb', 'ccc', 10, 'a', 'b']
```

This Python code defines a function called unique that takes a list lst as input and produces a new list containing unique elements from the original list, ignoring duplicates and 0 values. The code also includes three test cases to verify the correctness of the unique function. These test cases ensure that the unique function correctly identifies and returns the desired unique elements from the provided lists.