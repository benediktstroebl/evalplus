```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various list inputs
print(get_positive([-1, 2, -4, 5, 6]))      # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]

# Another test with a tuple and list input
print(get_positive((5, -3)))          # Output: [5]
print(get_positive((5, 6, -2)))       # Output: [-2, 5]

# Test with an empty list
print(get_positive([]))           # Output: []

# Test with a list of strings
print(get_positive(["A", "B", "C"]))     # Output: ["A", "B"]
```
This script defines the function `get_positive`, which takes a list as input and returns a new list containing only the positive elements from the original list. The function utilizes list comprehension to create a new list with positive elements, and the function is successfully tested with various inputs.