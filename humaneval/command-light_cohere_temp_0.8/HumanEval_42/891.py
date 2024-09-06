```python
def incr_list(lst):
    new_list = []
    for num in lst:
        new_list.append(num + 1)
    return new_list

# Basic test case
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 5])
test_incr_list.append([5, 3, 5])

# Verify function with test case
assert incr_list(test_incr_list) == test_incr_list[2:]

# Test case with different list
test_incr_list.append([5, 5, 3, 9, 2, 3, 3, 3, 9, 0, 123])

# Verify function with empty list
test_incr_list.append([])
assert incr_list([]) == []

# Test case with nested lists
test_incr_list.append([5, [1, 2, [3, 4]])

# Test case with custom items
test_incr_list.append(["one", [2, 3], 4])

# Test case with complex structure
test_incr_list.append([1, [2, [5, 6, 7]])
```