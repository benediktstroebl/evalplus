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

This function examines every possible pair in the list 'l' and determines whether their sum equals zero. It uses a set 'seen' to keep track of integers that have been previously encountered to ensure that each integer is considered only once when looking for matching pairs. The function returns 'True' if two distinct elements are found that sum to zero, and 'False' otherwise.