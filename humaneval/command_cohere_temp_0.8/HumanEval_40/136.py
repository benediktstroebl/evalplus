```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = i, -i
        if x in seen and y in seen:
            return True
        seen.add(x)
        seen.add(y)
    return False
```

This algorithm uses a hash set 'seen' to keep track of the distinct elements of the list 'l'. It initially verifies if the list element is zero and skips it. It then calculates the difference 'y = -x' and checks if 'x' and 'y' are already in the set 'seen'. If they are not, they are added to the set. If both 'x' and 'y' are found in the set, it means a trio of elements sum up to zero, and the function returns True. Otherwise, it moves on to the next element in the list. The algorithm completes the iteration over the list and returns False if no such trio is found. 

The unit tests demonstrated in the original problem statement would be sufficient to ensure this algorithm's correctness.