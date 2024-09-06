```python
def max_element(lst):
    if not_elements(lst):  # Remove empty list
        return None
    
    max_ = max(lst)
    return max

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    actual_max = max_element(test_list)
    assert actual_max == 123, "Assertion failed: maximum element is not the expected"

def not_elements(lst):
    return not len(lst) == 0

# Run the above script to test the function
```