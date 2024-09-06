```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with different lists
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123
# Use the function with a list of mixed numbers
mixed_list = [5, 35, -10, 45, -20, 3, 8, 7]
print("Mixed list:", mixed_list)
print("Maximum element:", max_element(mixed_list))

# Use the function with a list of empty list
empty_list = []
print("Empty list:", empty_list)
print("Maximum element:", max_element(empty_list))
``` 
This code provides a max_element function that accepts a list lst and returns the maximum element in the list using the built-in max() function. The test_max_element variable is a list that passes the test for the max_element function, and the code also prints the results.