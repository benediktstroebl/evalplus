```python
def sort_even(lst):
    return lst[:][::2] + lst[:-][1:]

# Test case 1:
test_suite = [1, 2, 3]
assertEqual(sort_even(test_suite), [1, 2, 3])

# Test case 2:
test_suite = [5, 6, 3, 4]
assertEqual(sort_even(test_suite), [3, 6, 5, 4])

# Test case 3:
test_suite = [10, 9, 5, 8]
assertEqual(sort_even(test_suite), [10, 9, 5, 8])

# Test case 4:
test_suite = [1, 3, 2, 4]
assertEqual(sort_even(test_suite), [1, 3, 2, 4])
```
The function `sort_even` takes a list as an argument and returns a new list with the elements from the original list that are even indices. The elements at odd indices are added back to the new list. The returned list is then sorted in ascending order.