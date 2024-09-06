```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test cases
test_get_positive = []
test_get_positive.py = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 6, 7, 8, 3]]

# Function and test cases
for test in test_get_positive:
    actual = get_positive(test)
    print(f"Test: {test}, Expected: {', ' '.join(actual)}")
```