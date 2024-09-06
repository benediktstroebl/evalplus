```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with various input
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(f"The list with positive numbers: {test_get_positive}")

# Call the function and print the result
print("The list with positive numbers: ", get_positive(test_get_positive))
```