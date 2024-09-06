Here is a Python script with a self-contained function that solves the problem you described:

```python
def triples_sum_to_zero(lst):
    if sum(set(t) for t in lst) <= 0:
        return True
    return False
```
Do you have any other questions about handling or improving code quality?