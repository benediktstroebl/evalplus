```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test case 1:
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test case 2:
empty_list = []
assert max_element(empty_list) == float('-inf')

# Test case 3:
single_element = [1]
assert max_element(single_element) == 1
```
The `max_element` function accepts a list as input and returns the maximum element in that list. The function raises a TypeError if the input is not a list. Also, three test cases are provided to ensure that the function behaves correctly.