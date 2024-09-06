Here is a Python script that includes the `pairs_sum_to_zero` function, which determines whether a list of integers can be summed to zero:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
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
    seen = set()
    for x in l:
        if x in seen:
            return False
        seen.add(x
    x)
    return True
```

This function accepts an array of integers and determines whether there are two distinct components in the array that, when added together, result in a total of zero. The function returns `True` if there are two elements that can be added to produce a sum of zero and `False` otherwise.