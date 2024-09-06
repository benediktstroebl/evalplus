```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.append([5, -5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_get_positive.append([5,])

print("Test List:", test_get_positive)
print()

# Function call
print(get_positive(test_get_positive))
```