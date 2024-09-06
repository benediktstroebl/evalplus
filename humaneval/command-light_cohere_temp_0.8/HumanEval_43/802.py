```python
def pairs_sum_to_zero(l):
    """
    Function to check if all elements in a list sum up to zero.
    """
   
    list of integers where the first element is positive and the rest are negative.
    """
    Returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """

test_pairs_sum_to_zero([1, 3, 5, 0])
	assert (False == pairs_sum_to_zero([1, 3, -2, 1]))
	assert (False == pairs_sum_to_zero([1, 2, 3, 7]))
	assert (False == pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
	assert (True == pairs_sum_to_zero([2]))
	assert (False == pairs_sum_to_zero([1]))
	return False
```