```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various inputs
print(get_positive([-1, 2, -4, 5, 6]))  # Expected Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected Output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a `get_positive` function that takes a list as input and returns a new list with only the positive numbers from the original input list. The function uses list comprehension to filter out the positive numbers from the input list. The test cases at the the end demonstrate that the function is working as expected with different inputs.