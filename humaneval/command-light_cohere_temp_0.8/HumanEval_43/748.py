```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
Return value: bool
    """
    seen = set()
    for num in l:
        if sum(seen) == 0:
            return False
        seen.add(num)
    return True
    ```