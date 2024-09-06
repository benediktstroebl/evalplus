```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assertEqual(max_element(test_max_element), 123)

# Test the max_element function with a list of strings
test_string = ["hi", "hello", "world"]
assertEqual(max_element(test_string), "hello")

# Test the max_element function with a custom max element
test_max = 123
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , test_max)
```