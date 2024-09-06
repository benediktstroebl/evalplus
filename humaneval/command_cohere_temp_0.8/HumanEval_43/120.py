```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This approach uses a set to keep track of elements encountered while looping through the list. For every positive element `x`, we add `x` to the set, and for every negative element `x`, we add `-x` to the set. If the set contains a element `x` (or `-x`) and there are at least two occurrences of `x` (or `-x`) in the list, then we return True, indicating the presence of two distinct elements that sum up to zero. Otherwise, we return False. It is worth noting that this approach has a time complexity of O(n) and performs well in terms of space complexity as well.

This problem can also be solved using `itertools.combinations` and `reduce`. Here's an example of that approach:
```python
def pairs_sum_to_zero(l):
    return any(reduce(lambda a, b: a + b, t) == 0 for t in itertools.combinations(l, 2))
```

This uses `itertools.combinations` to generate all pairs from the list and then checks if any of them sum up to zero.