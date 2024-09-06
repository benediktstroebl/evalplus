```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * n  # Initialize result list with zeros
    for i, x in enumerate(l): result[i] = x + 1
    return result

# Test the function with various inputs
test_cases = [
    [1, [1, 2, 3]],
    [5, [5, 3, 5, 2, 3, 3, 9, 0, 123]],
    [0, [9, 0, 9]]
]

for case in test_cases:
    actual = incr_list(case[1])
    expected = case[0]
    print(f"Case {case}: {actual} != {expected}")
```
The function incr_list takes a list l as input and returns a new list with the elements of l incremented by 1. The function uses the test cases with lists of different lengths and elements, and the expected output is compared with the actual output, and the test passes if the values match.