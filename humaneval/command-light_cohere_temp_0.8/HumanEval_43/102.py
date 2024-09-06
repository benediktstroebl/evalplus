```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    optimal time complexity: O(n)
    """
    if not l:
        return False
    if sum(l) == 0:
        return True
    for i in range(len(l)):
        if l[i] > 0:
            l.remove(l[i])
    else:
            break
    return False
```