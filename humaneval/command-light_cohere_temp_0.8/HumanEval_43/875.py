```python
def pairs_sum_to_zero(lst):
    # Return True if the list has two distinct elements whose sum is zero
    for i in range(1, len(lst)):
        if lst[i - 1] + lst[i] == 0:
            return True
    return False
```