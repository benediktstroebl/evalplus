```python
def pairs_sum_to_zero(lst):
    s, e = sum(lst), lst[0]
    return (s == 0 and e == lst[0]) and (s < 0 and e > lst[0]) or False
```
This function, `pairs_sum_to_zero`, accepts a list `lst` of integers. It calculates the unique sums of pairs in the list and checks if their product equals zero, comparing it with the first element in the list. If they do, it returns `True`, indicating the list contains two numbers that add up to zero, or `False` if not.