```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function to check max element of the list
def test_max_element(test_list):
    return max_element(test_list) == test_list[-1]

# Example list to test the function
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("The maximum element is:", test_max_element(test_list))
``` 
This code defines a max_element function that takes a list as input and returns the maximum element in the list. This is also provides a test function to check the max element of the list and an example list to test the function.