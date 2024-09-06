```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with different list inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Validate the function's output
for test in test_get_positive:
    assert get_positive(test) == test, "Function does not return correct positive numbers"
```