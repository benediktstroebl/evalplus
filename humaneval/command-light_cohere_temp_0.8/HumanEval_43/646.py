```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum to zero.
    """
    Returnss if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    Returns:
        list of integers
    """
    sum = 0
    for i in l:
        sum += i
    return sum == 0
```