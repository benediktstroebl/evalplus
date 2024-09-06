```python
def triples_sum_to_zero(lst):
    if sum(map(lambda x: abs(x - y for x, y in zip(lst, lst[1:])) if x != 0)) == 0:
        return True
    return False
```