```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
tests = {
    "Positive numbers list"
    "Negative numbers list"
    [
        "[-1, 2, -4, 5, 6]",
        "[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]"
    ]

for test_case in tests:
    actual = get_positive(test_case)
    expected = [num for num in test_case if num >= 0]
    print(f"Test case {test_case}: Expected: {expected}, Actual: {actual}")
```