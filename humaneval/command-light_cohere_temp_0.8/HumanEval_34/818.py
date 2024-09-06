```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 2, 'abc', 5, 3, 0]
assert unique(test_case2) == ['abc', 5, 3]

# Test case 3
test_case3 = [None, None, 5, 3]
assert unique(test_case3) == [5, 3]

# Test case 4
test_case4 = [5, 3, 'abc', 'b', 0, 'a']
assert unique(test_case4) == ['a', 'b', 5, 3]

print("All tests passed!")
```