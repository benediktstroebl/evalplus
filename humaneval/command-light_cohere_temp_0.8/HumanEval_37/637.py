```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    res = [x if x <= y else y for x, y in zip(even_list, lst)]
    return res

# Test cases
test_list = [1, 2, 3, 6, 4]
test_result = sort_even(test_list)
assert test_result == [3, 6, 5, 4]
test_list = [5, 6, 3, 4, 10, 20]
test_result = sort_even(test_list)
assert test_result == [3, 6, 10, 4, 20]
test_list = [3, 2, 20, 1, 4]
test_result = sort_even(test_list)
assert test_result == [2, 3, 1, 4]
```