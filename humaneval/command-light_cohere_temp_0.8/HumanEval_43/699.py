```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is much like a built-in function, but it's faster and easier to read.

"""
    return any(sum([x,y])==0 for x,y in set(l))
```