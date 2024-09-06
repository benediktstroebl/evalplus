```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	@example: [1, 3, 5, 0] returns False
	@example: [1, 3, -2, 1] returns False
	@example: [2, 4, -5, 3, 5, 7] returns True
	"""
    for el in l:
        if (el != 0) and (sum(l) == 0):
            return False
    return True
```