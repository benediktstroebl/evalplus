```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the code uses Python's `range` function to generate a sequence of numbers up to `n` and then maps these values to strings using `map`, joining the results together with spaces using `join`. This approach is more concise and efficient than using a list comprehension.

Here is a test case to verify the function behavior:
```python
test_cases = [(0, '0'), (5, '0 1 2 3 4 5')]
for n, expected in test_cases:
    assert string_sequence(n) == expected
```