```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic list with positive and negative numbers
assert max_element([1, 2, 3]) == 3

# Test case 2: List with positive number only
assert max_element([5]) == 5

# Test case 3: List with negative number only
assert max_element([-5]) == -5

# Test case 4: Basic list with mixed positive and negative numbers
assert max_element([3, -5, 2, 1]) == 3

# Test case 5: Empty list
assert max_element([]) == None
```
The code defines a function max_element that takes a list as input and returns the maximum element in that list using the max() built-in function. The code also includes several test cases to validate the behavior of the max_element function for different types of lists.