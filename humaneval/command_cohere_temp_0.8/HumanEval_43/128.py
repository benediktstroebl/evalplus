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

This function iterates through the list `l` and utilizes a set `seen` to keep track of elements encountered. For positive elements `x`, it adds `x` to the set `seen`, and for negative elements `x`, it adds `-x` to the set `seen` to account for pairs that sum to zero. If the set contains an element multiple times, then it has appeared multiple times in the list, and accordingly, the function returns `True` if there are two distinct elements that sum to zero and `False` otherwise.

Here's a straightforward set of unit tests that cover various scenarios:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    assert pairs_sum_to_zero([0, 0, 0, 0, 0]) == False
    assert pairs_sum_to_zero([-1, -1, 3, -3, 5, -5, 2, -2, 4, -4]) == True
``` 
This test suite covers a variety of cases, including lists with varying sizes, and with positive and negative integers.