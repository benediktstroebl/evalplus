```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] <= 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function employs two nested conditions for its evaluation:
1. The outer condition (`all(dups[num] <= 1 for num in dups)`) assesses whether there are duplicate entries in the list, ensuring there's at most one occurrence of each.
2. The inner condition (`all(num < nums[1] for num, nums in dups.items())`) checks whether the list is sorted. Here, each `num` is compared with the second element of the subsequent tuple `nums` to see if it's in ascending order.

The function returns `True` if the list is both sorted and has no duplicate entries. Otherwise, it returns `False`. 

The script also includes test cases to help ensure the function behaves as expected:
```python
def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 2, 3, 4])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([5])
    assert not is_sorted([1, 2, 3, 4, 5, 6])
``` 

To run the tests, you'd use the `pytest` framework, which needs to be installed separately, if not already. Once installed, you can execute the tests file using the command `pytest test_is_sorted.py`. 

This way, you can validate the functionality of the function and ensure it complies with the problem's specifications.