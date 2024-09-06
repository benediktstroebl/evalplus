```python
def triples_sum_to_zero(l: list):
    return sum(x for x in l if x in set(x for x in l)) <= 0
```
Do you have anything specific you would like to add or modify in this code?