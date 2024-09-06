```python
def max_element(lst):
    return max(lst)

# Basic test case
assert max_element([1, 2, 3]) == 3

# Lists with duplicates and negative numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Lists with specific elements
assert max_element([9, 8, 3, 2, 1, 5]) == 9
assert max_element([0, 2, 4, 7, 6]) == 4

# Lists with specific negative elements
assert max_element([-5, -3, -9, -2, -8, -4, -1]) == -9
```
This code defines a function max_element that calculates and returns the maximum element in a given list. It includes basic test cases, and also demonstrates handling lists with various elements, including duplicates and negative numbers.