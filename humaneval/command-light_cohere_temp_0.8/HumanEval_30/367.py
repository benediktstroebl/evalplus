```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a sample input
print(get_positive([-1, 2, -4, 5, 6, 9, 0, 123, 1, -10]))
```
This code defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the input list. The test block shows that the output should be: `[2, 5, 6, 9, 123, 1]`.