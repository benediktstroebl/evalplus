```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension with sum condition.
    """
    pair (1, 3) does not add to 0, 
    and pairs (2, 4) do add to 0.
    """  
    return sum(x for x,y in l if x+y <= 0) == 0
```