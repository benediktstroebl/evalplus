```python
def max_element(lst):
    if not_elements(lst):
        return None  # Handle empty list
    return max(lst, key=lambda x: x[1])  # Return largest element with non-negative value

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    actual = max_element(test_list)
    assert actual == expected, f"Actual: {actual}, Expected: {expected}"

def not_elements(lst):
    return not bool(all(map(lambda x: x <= 0, lst))))

# Run the tests
test_max_element()
``` 
This script defines a function max_element that finds the maximum element in a list, considering only non-negative values. It also includes a test_max_element() function to validate the correctness of max_element() by comparing its output against an expected result for a specific test list.