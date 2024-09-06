```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with different lists of numbers
test_get_positive_lists = []
test_get_positive_lists.zip '[-1, 2, -4, 5, 6]'
test_get_positive_lists.zip '["5", 3, " -5", "2", "-3", "3", "9", 0, "123", "1", "-10"]

print(f"This is the result of calling the function with the list of the values: {test_get_positive_lists}")

# Call the function and print the results
print(get_positive(test_get_positive_lists))
```