```python
def pairs_sum_to_zero(l):
    """
    checks whether a list of integers has two distinct elements that sum to 
    zero, returns True if this is the case, False otherwise.
    """
    function returns True if the list has two numbers that add up to zero and 
    is empty otherwise.
    """
return bool(sum(a+b for a,b in zip(*l)))
```