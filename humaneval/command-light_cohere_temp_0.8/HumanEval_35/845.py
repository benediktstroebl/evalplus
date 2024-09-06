```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_result = max_element(test_max_element)
assert test_result == 123
test_lst = [1, 2, 3, 4, -1]
test_result = max_element(test_lst)
assert test_result == 3
```
The function max_element takes a list lst as input and returns the maximum element in the list. It raises a error for non-list inputs. The test cases validate the
that the function correctly identifies the maximum element in both valid and invalid scenarios.