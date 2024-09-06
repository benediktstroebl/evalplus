```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list is sorted(), and the first three elements are returned and the sum is computed."""
    return sum(sorted(lst[:3])) == 0
```