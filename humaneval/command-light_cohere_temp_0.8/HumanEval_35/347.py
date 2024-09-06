```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with some data
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
max_result = max_element(test_max_element)
print("Maximum element:", max_result)

# Test with empty list
empty_list = []
empty_result = max_element(empty_list)
print("Maximum element of empty list:", empty_result)
```
This code defines a function max_element that finds the maximum element in a given list. It then tests this function with various inputs and prints the results.