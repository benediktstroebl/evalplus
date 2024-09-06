```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.extend(1)
    return [i+1 for i in l]

# Test cases
tests = [
    ("[1, 2, 3]", "[]"),
    ("[5, 3, 5, 2, 3, 3, 9, 0, 123]", "[6, 4, 6, 3, 4, 4, 4, 10, 1, 124]"),
    (["a", "b", "c"], "[][]"),
    (["aa", "bb", "cc"], "[aa, bb, cc]"),
]

for test_case, expected_result in tests:
    actual_result = incr_list(test_case)
    print(f"Test case: {test_case}, {actual_result}")
    print(f"Expected result: {expected_result}, ")
``` 
Do you need anything else I can help you with?