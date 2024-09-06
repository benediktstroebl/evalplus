```python
def triples_sum_to_zero(lst):
    # Using counters to count the number of elements and their sums.
    e = Counter(lst)
    s = Counter(elts_sum_to_n(lst) for elts_sum_to_n in combinations(lst, 2))
    return len(lst) == 3 and '0' in s and s['0'] == 1

def elts_sum_to_n(lst):
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == 0:
                    return (i, j, k)
    return None
```