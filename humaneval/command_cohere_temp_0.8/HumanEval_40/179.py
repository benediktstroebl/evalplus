```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b) not in seen:
                seen.add((a, b))
                if len(seen) == 3:
                    return True
    return False
```

The function `triples_sum_to_zero` works by checking every possible pair out of the given list `lst`. It initializes a set `seen` to track the seen pairs that sum up to zero. For every element `a` in the list, it iterates over the rest of the list, checking if `a + b + c` equals zero. If it does, it adds the pair `(a, b)` to the set `seen` and checks if the size of the set is now 3, in which case it returns `True`. Otherwise, it continues checking pairs iterating over the whole list. It returns `False` if no three distinct elements summing up to zero are found.