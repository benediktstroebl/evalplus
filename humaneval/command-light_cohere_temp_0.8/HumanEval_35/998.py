```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check the max element function
def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst1) == 123  # True

# Test function to check if max element works with list of integers
def test_max_element_ints():
    lst2 = [123, 45, 788, 2, 66, 90]
    assert max_element(lst2) == 123  # True

# Test function to check if max element works with list of floating numbers
def test_max_element_floats():
    lst3 = [123.456, 2.0, 3.1, -14.163875)
3.6
    assert max_element(lst3) == 3.14  # False
```
The code defines a function max_element that takes a list lst as an argument and returns the maximum element in the list. It then has three test functions test_max_element, test_max_element_ints, and test_max_element_floats that check that the max_element function works correctly with different types of lists.