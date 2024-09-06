```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
tests = [
    [
        "Input: [-1, 2, -4, 5, 6]
        "Expected Output: [2, 5, 6]"
    ]
]

test_results = get_positive(tests[0])
assert test_results == tests[1]  # Should pass
```