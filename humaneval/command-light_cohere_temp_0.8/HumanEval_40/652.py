```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    l.sort(reverse=True)
    for i, j in zip(l, l[1:]):
        if j+i>3 or j+i==0: continue
        else: break
    return "Yes" if sum(j+i for i, j in zip(l, l[1:]))==0 else "No"
```