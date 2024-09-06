```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with a list of various numbers
print(get_positive([-1, 2, -4, 5, 6]))  # Expected Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected Output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The function uses a essential filtering to retain only the positive numbers from the input. This ensures that the would be self-contained and doesn't rely on any external functions or modules for its implementation.