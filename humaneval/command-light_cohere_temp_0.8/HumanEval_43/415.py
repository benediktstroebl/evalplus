```python
def pairs_sum_to_zero(l):
    """
    checks whether the list has two elements whose sum is 
    zero, returns True if it does, and False otherwise.
    """
    list comprehension is very short way to do this!
    """
    return any([x+y for x, y in l if x != y else None]) == None
```