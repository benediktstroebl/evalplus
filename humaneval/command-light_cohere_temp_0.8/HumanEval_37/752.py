```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x + 1) % 2)

# Test case 1
test_list = [1, 2, 3]
test_result = sort_even(test_list)
assert test_result == [1, 2, 3]

# Test case 2
test_list = [5, 6, 3, 4]
test_result = sort_even(test_list)
assert test_result == [3, 6, 5, 4]

# Test case 3
test_list = [9, 3, 2, 8]
test_result = sort_even(test_list)
assert test_result == [2, 8, 3, 9]
```
The function `sort_even` takes a list `lst` as input and uses the `sorted` function with the `key` parameter set to a lambda function `(x + 1) % 2` that sorts the list elements based on the condition that their index is odd.

The lambda function checks if the current element's index `x` is odd. Then, the element is sorted into the first half of the list, while the elements with even indices are left as they are. The elements with even indices are sorted into the second half of the list, and the elements with odd indices are moved to the beginning of the second half.