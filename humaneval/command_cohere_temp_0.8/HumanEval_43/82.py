```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            if i in seen and l.count(i) > 1:
                return True
            seen.add(i)
        else:
            if -i in seen and l.count(-i) > 1:
                return True
            seen.add(-i)
    return False
```

This function examines every integer in the list, marking them as seen elements. If a positive integer is encountered, it checks if it has been previously seen and if there are multiple occurrences of this integer. If so, it returns `True`. This is done the same way but with negative integers. It returns `False` if no two elements sum to zero. This approach ensures that each integer is considered regardless of the list's order.