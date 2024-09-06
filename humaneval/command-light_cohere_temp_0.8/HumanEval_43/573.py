```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    two element sum to zero if they are two distinct elements in the list:
    1 and 3
    2 and 4
    -5 and -3
    5 and 5
    -2 and -1
    7 and 3
    """
    for i in range(len(l)):
        if l[i] in [l[i] for j in l[::2:]]:
            return False
    return True
```