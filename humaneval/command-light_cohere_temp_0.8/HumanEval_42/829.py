```python
def incr_list(lst):
    lst[::] = lst[-1] + 1
    return lst

# Test the function with a list with a single element
test_list = [1]
result = incr_list(test_list)
assert result == [1, 2]

# Test the function with a list with two elements
test_list2 = [5, 3]
result2 = incr_list(test_list2)
assert result2 == [6, 4]

# Test the function with a list of varying lengths
test_lists = [[1, 2], [2, 3, 4], [5, 6]]
for test_list in test_lists:
    result3 = incr_list(test_list)
    assert result3 == test_list[:-]
```