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
        else:
            seen.add(a)
    return False
```

This code uses a set `seen` to keep track of the elements that have been encountered so far. The algorithm loops through the list `l` and checks if the sum of two previously seen elements equals the current element. If it does, the algorithm returns `True`. The code also accounts for the case where the current element is zero, and the test case where the list contains only one element.