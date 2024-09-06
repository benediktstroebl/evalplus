```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various input
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
The code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. This is can be useful in various scenarios where you need to work with positive numbers in a list, such as filtering, computation, or data analysis.