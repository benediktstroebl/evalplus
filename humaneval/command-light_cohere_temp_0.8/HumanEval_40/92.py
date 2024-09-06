```python
def triples_sum_to_zero(l: list):
    if sum(set(sum(x) for x in l) & 1 == 0):
        return True
    else:
        return False
```
Do you need any assistance with anything else with this code?