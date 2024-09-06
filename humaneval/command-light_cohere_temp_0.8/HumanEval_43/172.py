```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test:
    assert l[-1] + l[-2] == 0, "Invalid input: two elements sum to non-zero"
    return True if l and all(x != 0 for x in l) else False
```