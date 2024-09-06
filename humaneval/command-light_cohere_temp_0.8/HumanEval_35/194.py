```python
def max_element(lst):
    if not_list(lst):  # Check if list is valid
        raise TypeError("Input must be a list")
    
    max_ = max(lst)  # Maximize the list using built-in max() method
    return max_

def test_max_element():
    test_lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected_result = 123
    result = max_element(test_lst)
    assert result == expected_result, "Expected max element {} but got {}".format(expected_result, result)

# Example usage
test_max_element()
``` 
This script defines a function `max_element` that takes a list as an argument, then checks the type of this list and returns the maximum element in the list.

Additionally, it has a function `test_max_element` that contains a test list and the expected result. Finally, an example is used to run these functions and pass the test.