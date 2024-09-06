Here's a self-contained Python script with a function that solves the problem of finding two elements in a list that sum to zero:
```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero,
    False otherwise.
    """
    function takes a list of integers as input and returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    s=set()
    for i in range(len(l)):
        if l[i] in s:
            return False
    s+=set([l[i]])
    return True
```