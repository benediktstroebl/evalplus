```python
def pairs_sum_to_zero(lst):
    total_sum = sum(lst)
    if total_sum < 0:
        return True
    return False
```
The function checks if the list's total sum is less than zero. If it is, the function returns `True`, indicating that there are two elements that sum to zero. Otherwise, it returns `False`.  This function is self-contained, and it can be easily reused in different code sections or modules.