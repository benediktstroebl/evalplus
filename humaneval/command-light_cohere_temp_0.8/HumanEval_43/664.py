```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    return any(sum(x) == 0 for x in l)
	``` 
This function checks whether two elements in the list sum to zero. If yes, it returns `True`, indicating that there are two elements in the list whose sum equals zero, and if not, it returns `False`.