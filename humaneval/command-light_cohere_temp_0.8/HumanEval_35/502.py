```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
for test_list in [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, -1,-4,-5], [1, 2, 3, -100]]:
    print(f"Maximum element of {test_list} is {max_element(test_list)}")
```
This code defines a function max_element that returns the maximum element in a given list. It takes a constant input list and gives the maximum value found using the `max()` function as the result.