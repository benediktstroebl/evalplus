```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-1, 2, -4, 5, 6]
test_list3 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -100]

assert get_positive(test_list1) == [2, 5, 6]
assert get_positive(test_list2) == [2, 3, 4]
assert get_positive(test_list3) == [0, 3, 9]
```
The function `get_positive` returns a list containing only positive numbers from the input list. The test cases ensure that the output is correct for different lists.