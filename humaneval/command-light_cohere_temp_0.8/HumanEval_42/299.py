```python
def incr_list(lst):
    lst[::] += 1
    return lst

# Test cases
test_incr_list = []
test_incr_list.push([1, 2, 3])
test_incr_list.push([5, [5, 3, 5, 2, 3, 3, 9, 0, 123]])

# Function tests
test_incr_list.assert print(functools.assert(incr_list(test_incr_list)))

# Output: [2, 3, 4]
```