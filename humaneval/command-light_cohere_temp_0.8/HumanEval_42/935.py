```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    return [lst[0] + 1, lst[1] + 1, lst[2] + 1]

# Test cases
test_incr_list = [
    (1,),
    (2, 3),
    (5, 3, 5, 2, 3, 3, 9, 0, 123),
]

# Test function
def test_func(test_case):
    assert incr_list(test_case) == test_case

for test_case in test_incr_list:
    test_func(test_case)
```