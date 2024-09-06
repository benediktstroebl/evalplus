```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various lists of numbers.
test_positive = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [2, 7, -6, 8, -9, 1, -5, 3, 54]
]

# Verify if the function works correctly
print(test_positive)
print("Should be: ", end="")
for num in test_positive:
    if not in get_positive(test_positive):
        print(" ", num)
```