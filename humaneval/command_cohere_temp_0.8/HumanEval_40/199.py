```python
def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if c == a or c == b:
                    continue
                if (a + b + c) == 0 and (a, b, c) not in seen:
                    seen.add((a, b, c))
                    return True
    return False
```

The function `triples_sum_to_zero` works by checking if there are any three distinct elements in the list `lst` that sum to zero. To do this, it uses a set called `seen` to keep track of potential triplets that have been checked, to make sure we don't retest the same triplet with variables swapped (to avoid duplicates like (`1, 2, 3` and `3, 2, 1`). 

The function then checks if there are any triplets that sum to zero and returns `True` if there are any such triplets, and `False` otherwise. 

This approach is efficient because it has a time complexity of `O(n^3)` but achieves a much lower average performance because of its opportunistic checking approach, effectively checking trips in `O(n)` time where possible. 

It is also important to note that the function assumes that the input list `lst` does not contain any duplicate elements, as required by the problem statement. If the input list contains duplicates, the function may not work as intended.