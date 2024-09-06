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

This function iterates through the list `l` and utilizes a set `seen` to keep track of integers encountered. When a positive integer is encountered, the function checks if it is in the set and whether it appears more than once in the list. If so, it returns `True`. The code then repeats this process for negative versions of the integers as a way to find pairs that sum to zero. 

This solution is efficient with a time complexity of O(n^2) due to the nested iteration over the input list.

The script can be complete with corresponding tests:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False

test_pairs_sum_to_zero()
```

This will ensure that the function's behavior corresponds to the problem statement and the given tests.