```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    """
    if sum(x for x in l if x != 0) <= 0:
        return True
    return False
```
This function takes a list of integers as input and returns "True" if there are two distinct elements in the list that sum to zero, and "False" otherwise. It uses a Verifiability to check if the sum of any two distinct elements is zero, and then returns the result.