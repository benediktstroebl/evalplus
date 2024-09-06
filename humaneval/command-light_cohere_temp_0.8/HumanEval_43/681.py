```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    Return True if they pair is a sum of zero and there are two distinct elements, and False otherwise.
    """
    elements are integers in the list
    """
    return sum(x) == 0 and len(set(map(lambda x: x, l)))) > 1
```