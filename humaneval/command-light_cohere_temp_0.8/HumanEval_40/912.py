```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> Test case 1
   
    []
    True
    >>> Test case 2
    [1, 3, -2, 1]
    False
    >>> Test case 3
    [1, 2, 3, 7]
    False
    >>> Test case 4
    [2, 4, -5, 3, 9, 7]
    True
    """
    s = set()
    for el in l:
        if len(s) < 3:
            s.add(el)
        else:
            return False
    return True
```