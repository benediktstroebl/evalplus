```python
def triples_sum_to_zero(lst):
    if not set(lst[:3]) == {0}:
        return True
    return False
```