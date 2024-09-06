```python
def triples_sum_to_zero(lst):
    """
    Checks if there are three distinct elements in the list that sum to zero.
    Returns: True if they, False otherwise.
    """
    triple_sum = sum(lst[0] + lst[1] + lst[2]) 
    if triple_sum == 0:
        return True
    return False
```