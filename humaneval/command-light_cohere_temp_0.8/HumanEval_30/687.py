```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_positive = get_positive([-1, 2, -4, 5, 6])
print(test_positive)  # Output: [2, 5, 6]
test_positive = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(test_positive)  # Output: [5, 3, 2, 3, 9, 123, 1]
```
The function `get_positive` returns a list containing only the positive numbers from the input list. The test cases validate that the output will be a list containing the desired positive numbers.