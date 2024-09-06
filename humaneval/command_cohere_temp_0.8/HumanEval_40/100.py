```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0:
            continue
        y_found, z_found = False, False
        for j, y in enumerate(l[i + 1:]):
            if y == 0:
                continue
            if x + y + l[j + 1] == 0 and x != y and j != i:
                y_found = True
                z_found = True
                break
        if y_found and z_found and (i, x, y) not in seen:
            return True
        seen.add((i, x, y))
    return False
```

The code employs a set to avoid repeating combinations and efficiently searches for combinations of three distinct elements that sum up to zero. The algorithm traverses the list twice: first to identify the potential first element of the triple, and upon finding a valid combination, the second traverse is executed to find the third element that completes the triple. The code checks for the presence of zero-valued elements and skips them to avoid infinite loops or performance issues. To ensure that the valid triples aren't repeated, the code adds each validated triple to the set.