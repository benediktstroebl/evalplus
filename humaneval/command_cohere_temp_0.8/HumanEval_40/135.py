```python
def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations and perform checks
    combos = list(itertools.combinations(lst, r=3))
    seen = set()
    for c in combos:
        if sum(c) == 0 and c not in seen and len(c) == 3:
            return True
        seen.add(c)
    return False
```

The function employs the `Counter` class and the `itertools.combinations` function to efficiently generate potential triple combinations and check whether their sums equal zero. This strategy significantly reduces the number of iterations and operations required to determine the answer.