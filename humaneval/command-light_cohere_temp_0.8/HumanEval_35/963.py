```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Maximum element:", max_element(test_max_element)) # Output: Maximum element: 123

# Test the function with a list of strings
test_str_element = ["haha", "hello", "world"]
print("Maximum element:", max_element(test_str_element)) # Output: Maximum element: hello
```