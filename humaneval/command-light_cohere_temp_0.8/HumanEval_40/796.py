```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    Returns: Boolean
    >>> triples_sum_to_zero([1, 3, -2, 1])
    Returns: True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    Returns: False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    Returns: True
    >>> triples_sum_to_zero([1])
    Returns: False
    """
    set1 = set(l)
    if len(set1) != 3: return False
    total = 0
    for num in l:
        total += num
    if total != 0: return False
    return True
```