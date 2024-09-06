```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in l such that their sum is 
    zero, and False otherwise.
    """
    return sum(x != y for x,y in zip(l)) == 0
```