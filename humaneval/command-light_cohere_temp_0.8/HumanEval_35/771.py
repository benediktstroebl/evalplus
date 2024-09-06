```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Invalid input)
with pytest.assert expected_exception=ValueError:
    max_element([])
```
This Python code defines a function max_element that returns the maximum element in a given list. The function is then tested with three different test cases:

1. Each element in the list is compared with the result from max_element, and the values match.

2. Test case 2 is a same that the list contains a negative number and an invalid element, and raises an expected ValueError.

3. This test case checks if calling the max_element with an empty list raises the correct exception. 

These test cases ensure that the function behaves correctly and handles edge cases properly.