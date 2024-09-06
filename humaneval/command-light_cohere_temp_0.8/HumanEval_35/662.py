```python
def max_element(lst):
    if not_elements(lst):  # Handle empty list
        return None
    
    max_val = max(lst)
    return max_val

def test_max_element(test_list):
    assert max_element(test_list) == 3  # Test positive list

def test_empty_list():
    assert max_element([]) is None  # Test empty list

def test_negative_elements():
    test_list = [-5, 3, -10]
    assert max_element(test_list) == 123  # Test negative list with positive max

def test_mixed_elements():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123]
    assert max_element(test_list) == 123  # Test list with mixed positive and negative elements

if __name__ == "__main__":
    print("Testing MaxElement function...")
    print("Test positive list: ", test_max_element([1, 2, 3]))
    print("Test empty list:", test_empty_list())
    print("Test negative list:", test_max_element([-5, 3, -10]))
    print("Test list with mixed positive and negative elements:", test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]))
```
This script defines a function `max_element` that finds the maximum element in a list, and three test functions that validate the `max_element` function.  The test_positive_list, test_empty_list, and test_negative_elements, respectively. The `if __name__ == "__main__"` statement ensures that the script is run only when executed directly, not imported.