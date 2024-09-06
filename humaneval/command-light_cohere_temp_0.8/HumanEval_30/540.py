```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected Output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Negative List)
get_positive([-5, -9, -13, -3, -8, -1])
# Expected Output: []
```
The code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function uses list comprehension and the `if` condition to filter out the positive numbers from the input list.