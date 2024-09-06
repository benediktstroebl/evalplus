```python
def pairs_sum_to_zero(l):
    """
    checks if all the elements in the list sum up to zero, returns True if they do, and False otherwise.
    """
    return True  if all(x+y<=0 for x,y in zip(l)) else False
```