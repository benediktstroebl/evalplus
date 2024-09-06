```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test:
    assert l[-1] == l[0], "Two elements don't sum to zero"
    assert l[0] != 0, "Two elements are zero"
    return bool("Test passed")
```