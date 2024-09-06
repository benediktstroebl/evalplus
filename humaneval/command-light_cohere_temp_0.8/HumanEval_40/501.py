```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst that sum to zero, False otherwise.
    """
    triple = list(set()) for num in lst:
        if num not in triple:
            triple.append(num)
    if len(triple) == 3:
            return True
    return False
```