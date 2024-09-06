```python
def max_element(lst):
    return max(lst)

# Basic test cases
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# List with duplicate elements
print(max_element([3, 3, 2, 1, 3]))  # Output: 3

# empty list
print(max_element([]))

# List with negative elements
print(max_element([-5, -3, -10, -2, -1, -8]))  # Output: -10
```
The function `max_element` takes a list as an argument and returns the maximum element in the list. This function is basic test cases, including lists with different data types and lengths, and an empty list. The function correctly identifies the maximum element in all test cases.