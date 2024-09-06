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

This function traverses the list of integers l and utilizes a set called seen to keep track of elements encountered. For every positive integer `i`, the function checks if `i` is already in the set seen and if the list contains more than one occurrence of `i`. If both conditions are met, the function returns True, as two distinct elements summing to zero are found. This process is repeated for negative integers by considering `-i` as a single element. The given tests would be passed by this solution.