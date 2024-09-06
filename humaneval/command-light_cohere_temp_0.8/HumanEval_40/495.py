```python
def triples_sum_to_zero(l):
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
    # Initialize variables
    n = len(l)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(n):
        sum1 += l[i]
        sum2 += l[i] * 2
        sum3 += l[i] * 3

    # Check conditions
    if sum1 == 0 and sum2 == 0 and sum3 == 0:
        return True
    return False
```