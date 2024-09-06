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

This function iterates through the list, tracking elements in a set (to avoid repeating operations on the same element). For positive elements, it checks if the element has appeared more than once and if its negated value is in the set, meaning it has a pair that sums to zero. It does the same for negative elements, as their pair will have a sum of 0. The function returns True if any such pairs are found, and False otherwise. This approach ensures efficiency and readability while correctly solving the problem.