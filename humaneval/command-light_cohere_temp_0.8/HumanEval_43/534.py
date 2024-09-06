```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether a list of integers is the sum of two distinct elements to zero.
    Returns True if the key is 'True'
    """
    return bool(''.join([x for x in l if x != 0 else x for x in l])
```