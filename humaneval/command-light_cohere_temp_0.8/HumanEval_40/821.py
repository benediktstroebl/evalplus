```python
def triples_sum_to_zero(lst):
    n = len(lst)
    if n < 3:
        return False
    sum_list = []
    for i in range(n):
        sum_list.append(lst[i])
    return sum_list in [0, -1, 2, 1, -2, 3]
```