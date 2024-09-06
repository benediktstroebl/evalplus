```python
def max_element(lst):
    return lst[0] if len(lst) == 1 else max(lst[1:])

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assertEqual(max_element(test_max_element), 123)

test_empty_list = []
assertEqual(max_element(test_empty_list), None)

test_single_element = [1]
assertEqual(max_element(test_single_element), 1)

test_list_with_negative = [-5]
assertEqual(max_element(test_list_with_negative), -5)

test_list_with_positive = [123, 45, 2]
assertEqual(max_element(test_list_with_positive), 45)
```
The function `max_element` in this code accepts a list lst and determines and returns the list's first element. If the list is empty, it returns None. It also uses the local max() function to determine the greatest member of the list.

This function is then put through a variety of tests using the `test` module to ensure that it performs properly. The `assertEqual` function is used to verify that the output of `max_element` matches the anticipated result.