```python
def pairs_sum_to_zero(l):
    # Count the number of pairs
    count = len(l) - l.count(0) - 1
    # Verify if any of the pairs sum up to zero
    for i in range(len(l)-1):
        if l[i] + l[i+1] == 0:
            return True
    return bool(count)
```

This function firstly calculates the number of pairs in the list `l` by subtracting 1 from the length of the list and then counting the number of zeroes in the list. Finally, it iterates over the list and checks if the sum of two adjacent elements is zero. If so, it returns `True`. If none of the pairs sum up to zero, it returns `False`.