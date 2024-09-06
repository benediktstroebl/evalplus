```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test cases
test_cases = [
    [(1, [1, 2, 3]), (2, [5, 6, 7])], (3, [10, 11, 12])], None]
]

for case in test_cases:
    actual = incr_list(case[0])
    expected = case[1]
    assert actual == expected, f"Test case {case[2]} failed"
```
This code defines a function `incr_list` that returns a list with elements incremented by 1. The function takes an input list `l` and uses list comprehension to create a new list with elements incremented by 1. The test cases are provided as well, which are assertions to check the correctness of the `incr_list` function against different input lists.