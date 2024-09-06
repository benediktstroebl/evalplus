```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [-float('inf'), -float('-inf')]]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [10, 2, 3, 8, 7, 5, 6],
    [2, 2, 4, 6, 6, 8, 10, 2],
    [-10, -5, -20, -30, -40]
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Input: {test_case}, Expected: {actual}")
```