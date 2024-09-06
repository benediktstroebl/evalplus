```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some examples
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
assertEqual(max_element([]) , 0)
assertEqual(max_element([1, 2, 3, 4, 5]) , 5)

```
This code defines a Python function max_element that takes a list l as input and returns the maximum element in the list. It uses the max() function to find the maximum element, which is then returned. The function is then tested with different lists to ensure it works correctly.