```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list is ordered set, and then it checks whether there are three elements with 
    opposite signs, and returns True if found.
    """
return not setdiff(lst, lst[::-1])
```