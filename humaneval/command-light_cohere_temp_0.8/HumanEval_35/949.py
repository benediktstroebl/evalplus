```python
def max_element(lst):
    return lst[0] if lst and lst[0] > all(lst[1:]) else lst[-1]

# Test case 1: Positive numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test case 2: Negative numbers
test_negative_numbers = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_negative_numbers) == -5

# Test case 3: Empty list
test_empty_list = []
assert max_element(test_empty_list) == float('-inf')

# Test case 4: Single element list
test_single_element = [3]
assert max_element(test_single_element) == 3
```
This code defines a function `max_element` that finds the maximum element in a given list. It uses the approach with early returns and tests the function with several cases: