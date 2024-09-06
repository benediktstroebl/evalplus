```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check the max element function
def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst1) == 123

# Run the test function
test_max_element()
``` 
This script defines a function `max_element` that returns the maximum element in a given list. It also includes a test function to check the correctness of the `max_element` function with a sample input list.