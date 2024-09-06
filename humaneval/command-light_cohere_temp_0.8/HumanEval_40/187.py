```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test_triples_sum_to_zero([1, 3, -2, 1])
    -> True
    """
    for el1, el2, el3 in zip(l, l, l):
        if sum(el1, el2, el3) == 0:
            return True
    return False
```