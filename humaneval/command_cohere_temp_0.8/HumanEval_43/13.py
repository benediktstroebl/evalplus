```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, x, seen):
    if x == 0:
        return True
    if x == 1:
        return False
    for y in l:
        if y == x or y == -x:
            if y not in seen and pairs_sum_to_zero(l, y, seen):
                return True
            if (-y) not in seen and pairs_sum_to_zero(l, -y, seen):
                return True
    return False
```

The function pairs_sum_to_zero uses a recursive approach to solve the problem. It takes an integer x, and a set seen to track seen and sum-partners of x. The integer x is always considered as a candidate pair. Additional candidates for the pair (x, -x) are also checked.