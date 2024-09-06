```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check max element of the list
def test_max_element(lst):
    m = max_element(lst)
    assert m == max(lst), f"Expected max({m}), got {max(lst)}"

# Example lists for testing
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([1, 2, 3, 4, 5])
test_max_element([6, 9, 2, 5, 3, 8, 7])
```
The code defines a max_element function that returns the maximum element in a list, using the built-in max() function. The test_max_element function tests the max_element with different lists and asserts that the result is correct. The code also provides an few examples of lists for testing.