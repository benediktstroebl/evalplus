```python
def unique(lst):
    return sorted(set(lst))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 3, 'abc', 5, '123', 0]
assert unique(test_case2) == ['abc', 5, '123']

# Test case 3
test_case3 = [0, 2, 3, 5, [1, 2, 3], [3, 4, 5, 6]]
assert unique(test_case3) == [0, 2, 3, 5, [1, 2, 3], [3, 4, 5, 6]]
```