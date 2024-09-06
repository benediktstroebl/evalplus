```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with sample inputs
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function called **get_positive** that takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses a simple list comprehension to filter out the positive numbers from the input list. The test section ensures that the function works correctly by passing different lists with various combinations of numbers and verifying if the output matches the expected results.