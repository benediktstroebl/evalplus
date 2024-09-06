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

This function examines every possible pair in the list `l` and uses a set `seen` to keep track of integers that have been seen. If a positive integer `x` is encountered, the function adds `x` to the set `seen`, and before moving on to the next integer, the function checks if the integer `x` has been seen more than once in the list `l` and if the sum of `x` and any other integer in the list adds up to zero. If so, the function returns `True`. The function plays out the same logic with negative integers, in case there is a pair of integers that add up to zero but in the opposite order, e.g. `-1` and `1`. If the loop ends without finding a pair that sums up to zero, the function returns `False`. 

Here is a test suite that can be used to validate the functionality of the code:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```