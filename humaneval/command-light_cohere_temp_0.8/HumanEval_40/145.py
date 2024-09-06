```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers is not sorted in any particular way.
    """
example:
    >>> triples_sum_to_zero([1,3,5,0])
    False
    >>> triples_sum_to_zero([1,3, -2, 1])
    True
    >>> triples_sum_to_zero([1,2,3,7])
    False
    >>> triples_sum_to_zero([2,4,-5,3,9,7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    s = 0
    for i in l:
        if s > 0 and i == s: s = 0
        elif s < 0: return False
        s += i
    return True
```