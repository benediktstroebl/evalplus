```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to pass in different lists and get the max element
def test_max_element(lst):
    m = max_element(lst)
    assert m == max(lst), f"Wrong maximum element: {m}, should be: {max(lst)}"

# Example 1
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Example 2
test_max_element([1, 2, 3, 4, 5])
```
The function max_element takes a list as input and returns the maximum element in the list. The test_max_element function tests the max_element function with different lists and asserts that the returned maximum element matches the maximum value of the input list. 

The max_element function also handles the case where the input list contains the maximum element itself, in which case it returns that element.