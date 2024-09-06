```python
def triples_sum_to_zero(l: list):
    """
    Function that checks if there are three distinct elements in the list that sum to zero.
    Returns: True if they can be achieved, and False otherwise.
    """
    Three distinct elements can sum to zero
    """
    if sum(set(l)) == 0:
        return True
    else:
        return False
```