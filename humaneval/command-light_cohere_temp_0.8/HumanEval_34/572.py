```python
def unique(lst):
    return list(set(lst))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, , 5, 2, 3, 3, 9, 0]
assert unique(test_case2) == [2, 3, 5, 9]

# Test case 3
test_case3 = [5, 2, 3, (1, 2)]
assert unique(test_case3) == [2, 3, 5]
```
The function unique is a self-contained solution to the problem. It utilizes the unique set with a list and returns the set of unique elements, which is then converted back to a list. This ensures that no external dependencies are required.