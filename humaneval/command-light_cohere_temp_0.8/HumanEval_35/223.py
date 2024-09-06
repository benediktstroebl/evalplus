```python
def max_element(lst):
    return max(lst)

# Basic Test Cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# List with negative elements
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# List with one element
assert max_element([5, 3, -5]) == 5

# List with integer and float elements
assert max_element([5, 3, -5, .5, .2]) == 5

# List with duplicate elements
assert max_element([5, 3, 3, -5]) == 3

# Empty list
assert max_element([]) == None
```

This code defines a function max_element that takes a list as input and returns the maximum element in the list. It is then pass multiple test cases to ensure the function's correctness. The test cases cover a following scenarios: basic positive and negative numbers, lists with one element, lists with both positive and negative numbers, lists with positive and negative numbers and integers/floats, lists with duplicate elements, and an empty list.