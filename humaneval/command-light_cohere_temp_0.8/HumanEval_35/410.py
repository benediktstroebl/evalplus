```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
# When list contains positive elements
print(max_element([1, 2, 3]))    # Output: 3

# Test case 2
# When list contains negative elements
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))   # Output: 123

# Test case 3
# When list contains multiple maximum elements
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, -4]))  # Output: 123
```
This Python script defines a function max_element that takes a list l as input and returns the maximum element in the list using the max() built-in function. The script also includes three test cases that validate the function's behavior, checking for positive, negative, and mixed positive and negative numbers.