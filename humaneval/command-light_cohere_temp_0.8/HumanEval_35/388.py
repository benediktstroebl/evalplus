```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

#Test cases
test_max_element = [
    ("List with negative numbers", [-5, 3, -10, 2, -3, 3, 9, 0, 123, 1, -100]),
    ("List with missing elements", [5, 3, -5, 2, -3, 3, nil, 9, 0, 123, 1, -10]),
    ("List with duplicate elements", [1, 2, 3, 3, 4, 5])

def test_function(test_case):
    """Test the max_element function with the given list."""
    assert max_element(test_case) == test_case[1], f"Error in {test_case[0]}: Expected {test_case[1]}, got {max_element(test_case)}"

test_max_element(test_case)
```