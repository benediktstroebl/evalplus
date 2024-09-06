```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    tests to solve the
    """
    test_passes = False
    for el in l:
        if el < 0:
            test_passes = True
            break
    return test_passes
```