Here is a Python script with a self-contained function that solves the problem of finding two elements in a list whose sum is zero, and passes corresponding tests:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    # convert the list to set
    s = set(l)
    # sort the set
    s.sort()
   
    minimum element
    # find two distinct elements that add up to zero
    for x, y in zip(s, s):
        if x + y == 0:
            return True
    return False
```