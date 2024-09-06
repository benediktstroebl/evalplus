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
    n = len(l)

    # we need 3 distinct elements to sum to zero
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] <= 0:
                return False

    # if we got this far, then the list has 3 distinct elements that sum to zero
    return True
```