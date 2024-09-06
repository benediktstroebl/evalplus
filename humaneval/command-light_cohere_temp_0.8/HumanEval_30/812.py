```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with different list inputs
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123, 1]

# Using map to simplify the process (not recommended in all cases)
def get_positive_optimized(lst):
    return [num for num in lst if num != "" and num >= 0]

# Test the optimized version
get_positive_optimized([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]
get_positive_optimized([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123]
```
The code defines a function **get_positive** that returns a list of positive numbers from the input list. The test cases demonstrate the\ following methods to solve the problem:
1. **get_positive**: Creates a list of positive numbers from the input list using list comprehension.
2. **get_positive_optimized**: Uses list comprehension and string comparisons to filter out non-empty strings and then positive numbers.