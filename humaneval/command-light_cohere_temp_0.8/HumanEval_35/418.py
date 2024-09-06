```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1:
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test case 2:
test_max_element = [1, 2, 3]
assert max_element(test_max_element) == 3
```
The above Python script defines a function max_element that aims to find the maximum element in the input list. It achieves this by utilizing the max() function to find the maximum value among the list elements. The test cases provide inputs that cover various scenarios, and they pass the tests successfully.