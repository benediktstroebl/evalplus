```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
# Returns true if the function works correctly
def test_max_element(test_list):
    return max_element(test_list) == max(test_list)

# Test lists with both positive and negative numbers
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-5, 3, 123, 2, -30, 5]

# Validate the function with test_list1
if not test_max_element(test_list1):
    print("Error: max_element function does not work correctly")

# Validate the function with test_list2
if not test_max_element(test_list2):
    print("Error: max_element function does not work correctly")
``` 
This Python code defines a function max_element that calculates and returns the maximum element from a given list. It also contains a test_max_element function, which validates the correctness of the max_element function using various input lists. The code then tests the validation functions with two different test lists and asserts whether the maximum element is correctly computed and returned by the max_element function.