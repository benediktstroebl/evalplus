```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    l = list(range(0,4))
    sum = 0
    for num in l:
        if sum == 0:
            return True
        sum += num
    return False
```