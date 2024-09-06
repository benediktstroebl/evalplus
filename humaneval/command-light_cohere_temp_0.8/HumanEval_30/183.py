```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various list inputs
# Test with a list containing all signs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print("List with negative numbers:", test_get_positive)
print()

print("List with positive numbers:", test_get_positive)
```