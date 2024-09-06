```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    example usage:
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    s1 = []
    s2 = []
    for i in l:
        if i < 0:
            s1.append(i)
        else:
            s2.append(i)
    if len(s1) == 0 or len(s2) == 0:
            return False
    elif len(s1) == 1 and len(s2) == 1:
        return s1[0] + s2[0] <= 0
    elif len(s1) == 2 and len(s2) == 1:
        return s1[0] + s2[0] <= 0 and s1[1] + s2[0] <= 0
    else:
        return False
    return True
```