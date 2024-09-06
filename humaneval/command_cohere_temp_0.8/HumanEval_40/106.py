```python
def triples_sum_to_zero(l: list):
    # Write your code here.
    seen = set()
    for a, b in itertools.combinations(l, 2):
        if a + b == 0 and (a, b) not in seen:
            seen.add((a, b))
            if len(seen) == 3:
                return True
    return False
```

This algorithm uses a set `seen` to keep track of already-seen pairs that sum to zero. For each pair `a`, `b` in the list, we try to add them to the set. If the set already contains three elements, meaning we've found three distinct pairs that sum to zero, the function returns `True`. Otherwise, it returns `False`. 

This is the simplest algorithm that solves the problem, but it has a time complexity of O(n^2) due to the nested loop structure and the check for each possible pair. There are more efficient ways to solve this problem using sorting and linear passes through the list.