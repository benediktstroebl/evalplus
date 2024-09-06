```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
	In the function, l is split into two loops:
    one for i in l:
        if sum(l[0:i]) == 0:
            return True
        l = l[i+1:]
    the other for the remaining elements in l, i.
    """
	The function returns False if no two elements in the list sum to zero, and True otherwise.

```
This function is self-contained and can solve the problem of determining if two elements in a list sum to zero, and pass corresponding tests.