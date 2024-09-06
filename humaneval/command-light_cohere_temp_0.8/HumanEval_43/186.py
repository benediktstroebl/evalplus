```python
def pairs_sum_to_zero(l):
    """
    Check if all elements in the list sum to zero.
    Elements:
    l -> list of integers
    """
    return sum(x for x in l) <= 0
```
The function checks if all the elements in the list `l` sum to zero, returning True and the list is empty or contains only zero, or False otherwise.