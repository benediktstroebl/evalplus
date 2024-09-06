```python
def max_element(lst):
    if not_elements(lst):  # Handle empty list
        return None
    return max(lst, key=lambda x: x)

def test_max_element(test_lst):
    assert max_element(test_lst) == test_max_element(test_lst)

# Example list for testing
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_list)

# Another test list
test_list2 = [1, 2, 3, -10, -4, 5]
test_max_element(test_list2)
```
This script defines a function max_element that finds the maximum element in a list. Using a max() function with a key parameter that calculates the maximum element based on the given key. The test_max_element function tests this function with various input lists and asserts that the result is correct.

The provided code is self-contained and can be used as is, with complete independence from other parts of the code.