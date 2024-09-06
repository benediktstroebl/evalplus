```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Edge case)
assert max_element([]) == None

# Test case 4
assert max_element([5, 2, -3, -100, -5]) == -100
```
The provided Python script defines a function max_element that aims to find the maximum element within a given list. It utilizes theator with a list and returns its maximum value using the built-in max() function. The code also includes several test cases to validate the correctness of the max_element function.