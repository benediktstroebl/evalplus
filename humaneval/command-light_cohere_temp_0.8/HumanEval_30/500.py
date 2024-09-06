```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with a sample list
test_get_positive = []
test_get_positive.push_back([-1, 2, -4, 5, 6])
test_get_positive.push_back([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Verify if the function returns the expected output
print(f"Test results:")
for test in test_get_positive:
    print(f"Input: {test}, Expected Output: [positive numbers]"
    print(f"  Actual Output: {get_positive(test)}"))
```