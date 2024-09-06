```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The function uses the `max` function, which returns the maximum value from a list of integers, to return the maximum element in the input list. 

This solution is straightforward and uses one of Python's built-in functionalities to solve the problem. It can be tested like this:
```python
TestMaxElement = unittest.TestCase('__main__)

def test_max_element(l):
    """Test max_element() function."""
    max_element_value = max_element(l)
    for element in l:
        if element >= max_element_value:
            trailed_value = element
    assert max_element_value == trailed_value

test_max_element([1, 2, 3])
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```