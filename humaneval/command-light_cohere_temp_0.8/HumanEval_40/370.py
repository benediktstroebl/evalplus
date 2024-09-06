```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> l = [1, 3, 5, 0]
    return_zero_sum(l)
    >>> l = [1, 3, -2, 1]
    return_zero_sum(l)
    >>> l = [1, 2, 3, 7]
    return_zero_sum(l)
    >>> l = [2, 4, -5, 3, 9, 7]
    return_zero_sum(l)
    >>> l = [1]
    return_zero_sum(l)
    """
def return_zero_sum(l):
    if sum(l) == 0:
        return True
    else:
        return False
```