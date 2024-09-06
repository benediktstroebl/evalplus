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

This function iterates through every element in the list and simply checks if the given number has a duplicate in the list in order to obtain a total sum of zero. It returns 'True' if such a pair is found, and 'False' if no such pair is found. This algorithm has a time complexity of O(n^2) due to the nested loop structure. An optimized approach could halve this complexity.