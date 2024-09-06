```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
"""
    # Check if the list has two distinct elements whose sum is less than 0
    for i in range(len(l) - 1):
        if l[i] + l[i + 1] < 0:
            return False
    return True  # if all sums are positive, return True
```