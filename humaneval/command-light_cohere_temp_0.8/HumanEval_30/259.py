```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    ("List with only negative numbers", [-1, 2, -4, 5, 6]),
    ("List with all positive numbers", [2, 5, 6, 123]),
    ("Mixed list with negative and positive numbers", [-5, 3, -10, 2, 9])
]

# Run the tests
for test_case in test_get_positive:
    assert get_positive(test_case[1]) == test_case[0]
```