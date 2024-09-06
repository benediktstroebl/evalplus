```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst that sum to zero,
    False otherwise.
    """
    triple sums = 0
    for i in range(3):
        if lst[i] != 0:
            triple sums += lst[i]
    return triple sums == 0
```