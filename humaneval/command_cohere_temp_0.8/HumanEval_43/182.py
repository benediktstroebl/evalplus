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

This function examines every possible pair in the list `l` and uses a set `seen` to keep track of integers that have been seen. If a positive integer `x` is seen more than once, the function evaluates to true if the following condition is met:
```
(x * -x) == 0
```
Which is true for any integer `x`. The case for negative integers is handled similarly. The function returns `False` if no such pair is found.

Here is a simpler alternative solution using `itertools.combinations`:
```python
import itertools

def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in itertools.combinations(l, 2))
```

This solution creates a generator which iterates through all pairs in the list using `itertools.combinations` and checks whether their sum is zero. The `any` function then checks if there are any such pairs and returns True or False accordingly.