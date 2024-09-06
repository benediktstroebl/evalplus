```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test drive function with various input.
def test_incr_list(l):
    assert l == [2, 3, 4]
    assert l[0] == 1  # Should add 1 to get 2
    assert l[-1] == 1  # Should add 1 to get 2, but handled by assertion

# Test with a list with 0 at the end.
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])

# Test with a list of strings.
test_incr_list(["aa", "bb", "cc"])
```