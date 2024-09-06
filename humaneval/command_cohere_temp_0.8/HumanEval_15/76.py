```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
test_cases = [
    (0, '0'),
    (5, '0 1 2 3 4 5'),
    (10, '0 1 2 3 4 5 6 7 8 9 10')
]

for n, expect in test_cases:
    assert string_sequence(n) == expect
```

This script includes a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-separated numbers starting from 0 up to and including `n`. The script also includes a list of test cases with corresponding expected outputs that validate the function.