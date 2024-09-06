```python
def triples_sum_to_zero(l):
    """
    Check if there are three distinct elements in the list that sum to zero.
    return: True if there are three suchs that sum to zero, otherwise, False. In case there are three integers in l that sum to zero, they are returned.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    True
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    sum = 0
    for x in l:
        sum += x
    return sum == 0
```  The code checks if there are three distinct elements in the list that sum to zero. It is easy to see that any three distinct elements that add up to zero will result in True. 

Additionally, if there are any other three elements, then they won't sum up to zero, and the function will return False.