```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function `is_sorted` checks for each number in the list whether it has more than one duplicate, and if so, whether all subsequent numbers are greater than the duplicate. The function returns `True` if the conditions are met for all numbers and `False` otherwise. 

The script can be tested as follows:
```python
# Test Cases
assert is_sorted([5])
assert is_sorted([1, 2, 3, 4, 5])
assert not is_sorted([1, 3, 2, 4, 5])
assert is_sorted([1, 2, 3, 4, 5, 6])
assert is_sorted([1, 2, 3, 4, 5, 6, 7])
assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
assert is_sorted([1, 2, 2, 3, 3, 4])
assert not is_sorted([1, 2, 2, 2, 3, 4])
``` 

The function can return the following values:
- `True` if the list is sorted
- `False` if the list is not sorted