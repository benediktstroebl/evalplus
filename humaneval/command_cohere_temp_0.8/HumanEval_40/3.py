```python
def triples_sum_to_zero(lst):
    # Use sorting to cluster elements with the same value
    sorted_lst = sorted(lst)
    grouped_lst = [list(group) for group in itertools.groupby(sorted_lst)]

    for a, b, _ in combinations(grouped_lst, 3):
        if a[0] + b[0] == 0:
            return True

    return False
```

The code sorts the list and then uses `itertools.groupby()` to group elements according to their value. It then loops over all combinations of these groups of three (using `combinations()`) and checks whether the sum of the first element of each group equals zero. If so, it returns `True`, and if not, it returns `False`.