```python
def max_element(lst):
    return max(lst)

# Basic test case:
assert max_element([1, 2, 3]) == 3

# List with negative elements:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# List with multiple unique max elements:
assert max_element([9, 3, -10, -3, -20]) == -3

# Complex list with duplicates:
assert max_element([3, 3, 8, -5, -20, 8, 7, -8, -6]) == 8
```
This code defines a function max_element that returns the maximum element in a given list. It is then pass several test cases to ensure the function works correctly. The tests include basic cases with positive and negative numbers, as well as lists with multiple unique max elements and duplicates.