Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of scripting common list operations. It goes through each element in the input list `l` and creates a new list with only the elements that are greater than zero. 

The result of the list comprehension is assigned to the return function, meaning that the function will output the new list created through the list comprehension. 

This function is self-contained, meaning that it does not depend on any external variables or classes, and it can stand on its own in a markdown code block. 

Here's how you can test this function against the given use cases:
```python
# Test 1: [-1, 2, -4, 5, 6]
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test 2: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
The above tests assert that the function `get_positive()` returns the expected values for the given input lists. 

This script provides a self-contained function that solves the problem of filtering out positive numbers from a list, and it can be easily embedded in a markdown code block.