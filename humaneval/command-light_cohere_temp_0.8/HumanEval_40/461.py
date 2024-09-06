```python
def triples_sum_to_zero(l: list):
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
    for el in l:
        if not_three_sum_zero(l[:2] + [el]) == False:
            return False
    return True

def not_three_sum_zero(l: list):
    """
    checks whether there are three distinct elements in the list that sum to zero
    """
    sums = []
    for i in range(len(l)):
        sums.append(l[i]) + l[i+1]
    if len(set(sums)) != 3:
        return False
    return True
```