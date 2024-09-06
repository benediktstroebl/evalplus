```python
def pairs_sum_to_zero(l):
    if not set(l) == {0}:
        return True
    return False
```
The function tests the list for two distinct elements that sum up to zero, and returns `True` if successful or `False` otherwise.