```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a != 0:
            if (0, a, -a) in seen:
                return True
            seen.add((a,))
            if (a, -a) in seen:
                return True
            seen.add((-a,))
    return False
```

This approach uses a set data structure to keep track of seen elements. It has a time complexity of O(n^2) where n is the length of the input list.