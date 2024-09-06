```python
def triples_sum_to_zero(lst):
    """
    Function that checks if there are three distinct elements in the list that sum to zero, and returns True or False.
    """
    sum(x * y * z for x, y, z in lst) 
    if sum((x+y+z) for x, y, z in lst) == 0:
        return True
    else:
        return False
```