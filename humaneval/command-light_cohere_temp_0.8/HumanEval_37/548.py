```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x, x + 1))

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 10, 2, 3],
    [20, 15, 5, 6]
]

for test_case in test_cases:
    result = sort_even(test_case)
    assert result == test_case
```