```python
def triples_sum_to_zero(l: list):
    return any(sum(t) == 0 for t in zip(*l)))

# Test the function with various inputs
for i in [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 9],
    [1],
]:
    assert triples_sum_to_zero(i) == True
```