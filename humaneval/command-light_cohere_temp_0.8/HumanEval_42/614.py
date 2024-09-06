```python
def incr_list(lst):
    lst[0] += 1
    for num in lst[1:]:  lst[num] += 1
    return lst

# Test the function with various inputs
test_incr_list = [1, 2, 3]
test_incr_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list3 = [(), [], [1, 2, 3] ]

# Verify the function returns the expected results
assert(incr_list(test_incr_list) == [2, 3, 4])
assert(incr_list(test_incr_list2) == [6, 4, 6, 3, 4])
assert(incr_list(test_incr_list3) == [2, 3, 4])

# Test the function with negative increment and empty list
test_incr_list4 = [5, 3, 5, 2, 3, 3]
test_incr_list5 = []

# Verify the function handles negative increments and empty lists correctly
assert(incr_list(test_incr_list4) == [5, 3, 5])
assert(incr_list(test_incr_list5) == [5, 3, 5])
```