```python
def pairs_sum_to_zero(l):
    """
    Function to check whether all elements in the list sum to zero.
    >>> r = [int_list] + [0]
    >>> r == [1, 0]
    True
    >>> r = [1, 3, -2, 1]
    >>> r == [1, 0]
    True
    >>> r = [1, 2, 3, 7]
    >>> r == [1, 0]
    True
    >>> r = [2, 4, -5, 3, 5, 7]
    True
    >>> r = [1, 2, 3, 7]
    >>> r == [1, 0]
    True
    """
    if sum(l) == 0:
        return True
    return False
```  The function performs a basic check to see if there are two elements in the list that sum up to zero, and returns True if this is the case, and False otherwise.