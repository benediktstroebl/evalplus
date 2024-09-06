```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with a sample input
# Print the result
print(get_positive([-1, 2, -4, 5, 6]))
```