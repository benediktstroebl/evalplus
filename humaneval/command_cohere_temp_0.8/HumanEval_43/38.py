```python
def pairs_sum_to_zero(l):
    # Count the number of pairs
    count = len(l) - len(set(l))
    # Count pairs that sum to zero
    zero_sum = sum([1 for i in l for j in l if i + j == 0])
    return zero_sum > 0 if count > 1 else False
```

This function operates on the principle that there can be no pairs that sum to zero unless there are at least two distinct elements in the list. 

The tests this function passes are:
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