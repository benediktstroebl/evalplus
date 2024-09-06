```python
def pairs_sum_to_zero(lst):
    sum = 0
    for x, y in lst:
        if x + y == 0:
            sum += 1
        else:
            sum += 0
    return sum == 0
```