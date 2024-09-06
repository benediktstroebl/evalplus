```python
def triples_sum_to_zero(l):
    """
    Function to check if all three elements in the list sum to zero
    """
    if sum(x for x in l) == 0:
        return True
    else:
        return False
```