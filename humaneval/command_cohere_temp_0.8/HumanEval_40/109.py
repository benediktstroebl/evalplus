```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a == 0:
            continue
        if len(seen) == 2:
            if a + seen.pop() + seen.pop() == 0:
                return True
        elif a not in seen and len(seen) < 2:
            seen.add(a)
        else:
            seen.clear()
    return False
```

This algorithm works by repeatedly looking for two elements in the seen set and checking if the third element that completes the triple equals zero when added to the other two elements. The seen set is used to keep track of elements we've encountered, and we reset it when we encounter a third element that doesn't work with one of the previous two elements. The algorithm also ignores zeroes in the list, as triples involving zeros will always sum up to zero.

This solution has a time complexity of O(n), where n is the length of the input list `l`, as it iterates through the list once, and for each element, it performs a constant amount of operations, primarily involving set operations and comparisons.