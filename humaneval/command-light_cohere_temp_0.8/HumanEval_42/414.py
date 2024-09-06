```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

#Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [10, 11, 12, 13]
]

# Function call and result validation
for test in test_incr_list:
    actual = incr_list(test)
    assert actual == test
```