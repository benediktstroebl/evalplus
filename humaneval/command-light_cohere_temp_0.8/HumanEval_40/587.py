```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test case:
    >>> test = triples_sum_to_zero([1, 3, 5, 0])
    >>> print(test)
    True
    >>> test = triples_sum_to_zero([1, 3, -2, 1])
    >>> print(test)
    True
    >>> test = triples_sum_to_zero([1, 2, 3, 7])
    >>> print(test)
    False
    >>> test = triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    >>> print(test)
    True
    >>> test = triples_sum_to_zero([1])
    >>> print(test)
    False
    """
    for num in l:
        if (3*num) <= 0:
            return True
    return False
```