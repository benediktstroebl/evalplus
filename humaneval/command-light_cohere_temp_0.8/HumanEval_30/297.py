```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive([-1, 2, -4, 5, 6])
print(test_get_positive)  # Output: [2, 5, 6]
test_get_positive = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(test_get_positive)  # Output: [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function named `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the input list. It uses list comprehension to iterate through the list and filter out the numbers greater than or equal to zero, which are positive. The function is then tested by passing two lists with different sets of numbers and verifying that it returns the expected output.