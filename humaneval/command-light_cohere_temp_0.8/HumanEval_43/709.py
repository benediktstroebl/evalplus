```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    return True if there are two elements that sum to zero, and False otherwise.
    """
    sorted(l)
    l.count_two_sum_to_zero = 0
    for x in l:
        if x in l.count_two_sum_to_zero:
            l.count_two_sum_to_zero += 1
        else:
            l.count_two_sum_to_zero += 1
            if l.count_two_sum_to_zero == 2:
                return True
    return False
```