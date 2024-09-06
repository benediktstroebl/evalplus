```python
def pairs_sum_to_zero(l):
    return sum(x for x in l if x not (-x)) == 0
```
This Python function checks each element against itself to determine if it can be used to create zero. The function returns True if the result is True, and False otherwise.