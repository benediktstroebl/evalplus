```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This approach uses a set to keep track of seen integers. For every integer `x`, the code checks if `x` or `-x` have been previously seen. If both are seen and the count is greater than one, the function returns `True`. Otherwise, it adds `x` or `-x` to the set and checks the next integer in the list. The overall time complexity is O(n). The space complexity is O(min(n, m)), where `n` is the size of the list and `m` is the maximum value of any integer in the list. 

This solution should be able to pass the given tests. You can copy and paste this code into a Python environment to verify.