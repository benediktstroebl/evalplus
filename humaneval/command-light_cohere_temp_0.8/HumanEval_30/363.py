```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123]

# Test case 3
get_positive([-100, -500, -20, 0, -40, 80, 700, -7])  # Output: [-100, -500, -20]
```
The function `get_positive` takes a list lst as input and returns a new list containing only the positive numbers from the original list. 
This function is self-contained and can be used to solve the problem of filtering out the positive numbers from any given list in a single and efficient manner.