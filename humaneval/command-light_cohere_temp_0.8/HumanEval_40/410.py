```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test1
    input
    [1, 3, 5, 0]
    False
    >>> test2 = [1, 3, -2, 1]
    True
    >>> test3 = [1, 2, 3, 7]
    False
    >>> test4 = [2, 4, -5, 3, 9, 7]
    True
    >>> test5 = []
    False
    """
    for el in l:
        sum_so_far = sum(l)
        if sum_so_far < 0: return False
    return True
```