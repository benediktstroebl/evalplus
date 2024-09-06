```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
test_max_element = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print("Maximum element:", test_max_element)  # Output: Maximum element: 123

# Test list inputs
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element = max_element(test_list)
print("Maximum element:", test_max_element)  # Output: Maximum element: 123
```

The above Python script defines a function max_element that returns the maximum element in a given list. It then tests the general function using a list of numbers, and the result is printed. The function passes all the specific test cases without using any external functions or modules. The self-contained nature of the function allows for easy reuse in various scenarios.