```python
def pairs_sum_to_zero(l):
    """
    checks if all the elements in the list sum to zero.
    """
    Returnss True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test:
    assert all([x != y for x, y in zip([1,3,5])]) 
    assert all([x + y != 0 for x, y in zip([1,3,5])])
    assert l == [1,3,5]
    assert l[0] + l[1] == 3 and l[1] + l[2] == 5 and l[3] + l[4] == 0
    assert l[0] + l[3] == 0
    assert l[1] + l[4] == 5
    return True
```