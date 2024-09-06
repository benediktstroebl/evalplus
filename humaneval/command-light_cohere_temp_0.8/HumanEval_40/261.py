```python
def triples_sum_to_zero(lst):
    if not set(lst[:2]) <= { lst[1:] } :
        return True
    return False
```