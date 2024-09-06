```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(val > 0 for val in lst)

# Test case 1
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element_res = max_element(test_max_element)
should_be = float('inf')
assert test_max_element_res == should_be, "Test case 1 failed."

# Test case 2
test_max_element = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element_res = max_element(test_max_element)
should_be = 123
assert test_max_element_res == should_be, "Test case 2 failed."
```
This code defines the `max_element` function that takes a list as input and returns the maximum element in the list. It also defines a a function `not_positive` to check if the list contains only positive values, and if not, returns `float('-inf')` as the maximum element. 
Then, the code runs two tests with different lists to check if the `max_element` function is working correctly.