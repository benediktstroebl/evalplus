```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension in this function is the core to the algorithm.
    """return "False" if there is no pair of elements in the list that sum to zero,
    otherwise return "True" 
    """
return sum(x for x in l if x != 0) == 0
```