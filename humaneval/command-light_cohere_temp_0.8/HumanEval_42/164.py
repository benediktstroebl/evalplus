```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test cases
test_incr_list = [
    [(1, [1, 2, 3])],
    [(2, [5, 3, 2])],
    [(3, [15, 12, 11])],
    [(4, [])],
    [(5, [9, 8, 7])],
]

for case, test_list in test_incr_list:
    actual_result = incr_list(test_list)
    expected_result = case[1]
    assert actual_result == expected_result, f"Test {case[0]} failed"
``` 
This code defines a function `incr_list` that incrementally every element in the input list by 1. The function is tested using 5 test cases, each containing an input list and the expected output.