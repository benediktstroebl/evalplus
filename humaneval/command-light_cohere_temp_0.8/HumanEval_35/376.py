```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function with different types of lists
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3  # This should be the same as before
    assert max_element([-5, -3, 3, -10]) == -3
    assert max_element([0]) == 0
    assert max_element([123]) == 123
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([-1, -10, -100, -baby]) == -100

    # Test the function with empty list
    assert max_element([]) == None
```
This script defines a function `max_element` that takes a list as an argument and returns the maximum element in the list. It also includes a test cases to verify the correctness of the `max_element` function with different types of lists and empty lists. The test cases cover various scenarios and ensure that the function behaves as expected.