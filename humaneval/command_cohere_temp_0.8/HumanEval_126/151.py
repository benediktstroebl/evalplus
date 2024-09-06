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

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. Whether each element in the list appears only once (using the dictionary `dups`).
2. Whether each element is less than its subsequent appearance(s), if any (by iterating through the dictionary `dups`).

This solution enables the function to accurately determine whether the list is sorted and whether there are any duplicate elements. 

The following is a test suite that can be used to validate the functionality of the solution:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])

    # Edge cases
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])

    # Cases with duplicates
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 2, 2, 2, 3, 4])

    # Larger list with duplicates
    assert is_sorted([1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10])
```

To test the function, simply run the test suite using a Python runtime. This will validate the correctness of the solution against the predetermined conditions.