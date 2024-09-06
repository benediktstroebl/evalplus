```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    assert len(result) == n+1, f"Result list length mismatch: {len(result)} != {n+1}"
    return result

# Test the function with various inputs
test_cases = [
    ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]),
    ([], []),
    ([6, 4, 6], [6, 4, 6, 7, 8, 9])
]

for case in test_cases:
    result = incr_list(case)
    print(f"Input: {case} -> Output: {result}")
```

This script defines a function `incr_list` that returns a list with elements incremented by 1. The function is then tested with various inputs using a `test_cases` list, and the results are printed.