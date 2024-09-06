```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            y = -x
        else:
            y = x
        if y in seen and l[seen.index(y)] != l[i]:
            return True
        seen.add(x)
    return False
```

This algorithm employs a simple enumeration technique. It iterates through the list, checking if each element has a pair that can be subtracted to sum up to zero. The seen set is used to keep track of the elements that have been encountered while searching for the second number that completes the triple. The function returns True if a triplet is found and False if the search is unsuccessful.