```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
tests = [
    [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [0]]

for test_case in tests:
    actual = get_positive(test_case)
    print(f"Test case {test_case} expected: {', '.join(actual)}")
```