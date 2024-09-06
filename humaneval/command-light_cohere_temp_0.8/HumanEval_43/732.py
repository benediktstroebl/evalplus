```python
def pairs_sum_to_zero(l):
    """
    checks if there are two distinct elements in the list that sum to zero.
    if sum(x[::2]) == 0:
        return True
    else:
        return False
```
This function takes a list of integers as input and returns True if there are two distinct elements in the list that sum to zero, and False otherwise. The function works by checking if the sum of the first two elements in the list is equal to zero. Then, it checks the last element in the list, and so on until it reaches the second boundary.