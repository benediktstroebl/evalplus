```python
def pairs_sum_to_zero(l):
    """
    checks if all pairs of numbers sum to zero.
    """
    returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
assert(len(l) > 2), "Input list must have more than two elements.")
    assert not any(x in l for x in [-2, l[0]]), "First element must be positive"
    assert l[0] + l[1] == 0, "Sum of two elements should be zero"
    return True
```