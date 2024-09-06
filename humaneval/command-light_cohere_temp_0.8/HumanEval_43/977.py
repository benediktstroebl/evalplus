```python
def pairs_sum_to_zero(l):
    """
    Returns True if all the elements in the list sum up to zero,
    False otherwise.
    """
    lst = l[:]
    sum = 0
    for i in l:
        sum += i
    return sum == 0
```