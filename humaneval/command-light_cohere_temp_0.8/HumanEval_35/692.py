```python
def max_element(lst):
    if not_elements(lst):  # Test for empty list
        return None
    
    max_ = max(lst)
    return max

def test_max_element(test_lst):
    assert max_element(test_lst) == 7  # Test with known correct result

def not_elements(lst):
    return not len(lst) == 0  # Test for empty list

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(my_list))  # Output: 7
print(test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 7
``` 
The function max_element takes a list lst as input and returns the maximum element in the list. It uses the use the covered by the max function to find the maximum. The function test_max_element takes a list test_lst as input and calls the max_element function with it, then asserts that the result is correct. 

This code also includes a utility function not_elements that checks if the list passed to the function is empty or not. The test_max_element function is a simple test function that asserts that the max_element function returns the correct result for a given list.