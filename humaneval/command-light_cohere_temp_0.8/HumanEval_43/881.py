```python
def pairs_sum_to_zero(l):
    """
    Check if list has two distinct elements that sum to zero.
    return True if there are two elements that sum to zero, 
    and False otherwise.
    """
    test cases
    For valid inputs.
    """
return False  # No solution for lists with 0 or 1 elements.
    return any([ele for ele in l if ele != l[-1] + ele]) and False
    for ele in l:
        if ele == l[-1] + ele:
            return False
    return True
```