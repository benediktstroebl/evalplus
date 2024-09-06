```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y == 0 and i != j:
                    if i < j and (i, j) not in seen:
                        seen.add((i, j))
                    elif j < i and (j, i) not in seen:
                        seen.add((j, i))
                    else:
                        return False
                    if len(seen) > 2:
                        return False
                else:
                    return False
            return False
        else:
            for j, y in enumerate(l[i+1:]):
                if x + y == 0 and i != j:
                    if i < j and (i, j) not in seen:
                        seen.add((i, j))
                    elif j < i and (j, i) not in seen:
                        seen.add((j, i))
                    else:
                        return False
                    if len(seen) > 2:
                        return False
                else:
                    return False
            return False
    return False
```

The algorithm works by using two nested loops to check all possible triples. The generator recursively eliminates duplicates by checking if the seen set already has the considered combination or its permutation. The generator returns False if it finds two distinct pairs that sum up to zero or if the seen set has more than 2 elements, guaranteeing that there is a third element that completes the triple.  Otherwise, it returns True. It is worth noting that the algorithm's time complexity is O(n^3), where n is the list's element count.