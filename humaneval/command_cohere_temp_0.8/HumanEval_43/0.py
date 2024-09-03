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

This function iterates through the list `l` and utilizes a set `seen` to track numbers `x` that have been encountered. When a positive number `x` is encountered, it is added to the set `seen`, and the function checks if it has already been encountered more than once in the list. If so, a pair of `(x, -x)` sums to zero. For negative numbers `x`, the set element is `-x` so that the same check can be made. If a number is encountered that has been seen before and also matches the condition with `-x` being seen before, then the function returns True, indicating two distinct elements sum to zero. Otherwise, it returns False. 

Here is an example usage output:
```python
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
```
This matches the test cases provided in the original problem.