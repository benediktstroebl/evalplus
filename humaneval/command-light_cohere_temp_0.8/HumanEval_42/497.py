```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [0]

# Test case
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_res = incr_list(test_incr_list)
test_eq(test_incr_list_res, [6, 4, 6, 3, 4, 4, 10, 1, 124])

# Descriptive comments using the docstring syntax
# doc_comment_example
def doc_comment():
    """This is a docstring comment."""
    pass
```