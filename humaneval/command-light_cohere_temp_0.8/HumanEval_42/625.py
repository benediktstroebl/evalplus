```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [i + 1 for i in l] + [n + 1]
    return res

# Test cases
test_incr_list = [
    (=[1, 2, 3], incr_list),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], incr_list),
    ([], incr_list),
    ([10, ], incr_list),
    ([10, 2, 3, 4], incr_list),
]

# Main function
def test_func(test_case):
    assert list(test_case) == test_incr_list(test_case)

if __name__ == "__main__":
    test_func(test_incr_list)
```