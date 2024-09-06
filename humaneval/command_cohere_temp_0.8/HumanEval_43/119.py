```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and (i - 1) in seen:
            return True
        seen.add(i)
    return False
```

This function examines each integer in the list, using a set data structure to efficiently track which integers have already been encountered. Specifically, it checks if the current integer is greater than zero and not already in the set, and if so, it checks if the difference of the current integer and 1 is in the set. This technique efficiently determines if the current integer together with its difference by 1 adds up to zero, without double-checking pairs that have been previously identified.