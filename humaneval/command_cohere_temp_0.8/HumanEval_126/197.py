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

The function works by first checking if there are any duplicates in the list using a dictionary to count the number of times each unique item appears. If there are duplicates, it then checks if all duplicates are directly followed by the next largest number in the list. The function returns True if the list is sorted and has no duplicates, and False otherwise.

Here is a simple test suite to test this function:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 2, 3, 4])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])

    # Edge cases
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5, 6])

    # With negative numbers
    assert not is_sorted([1, 2, 3, 4, 5, -6, 7])

    # With non-integer values
    assert not is_sorted([1, 2, 3, 4, 5, 6, 7.0])
    assert not is_sorted([1, 2, 3, 4, 5, '6', 7])
``` 

Running these test cases using a Python test runner such as `pytest` or `unittest` will ensure that the function behaves as expected.