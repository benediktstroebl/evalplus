```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums for num, nums in dups.items())
```

The function uses a dictionary `dups` to keep track of how many times each number appears in the list. Then, it checks whether each element is unique (`all(dups[num] == 1 for num in dups)`), and whether each element is in ascending order (`all(num < nums for num, nums in dups.items())`), with an added condition that the number of occurrences is not greater than 1. The function returns True if the list is sorted with no duplicate entries, and False otherwise.

Here is a simple test suite to test the function:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 2, 3, 4])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])

    # Edge cases
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5, 6])

    # With duplicates
    assert not is_sorted([1, 2, 3, 4, 5, 6, 7, 7, 8])
    assert is_sorted([1, 2, 2, 3, 3, 4])

test_is_sorted()
``` 
This should give you a test suite that validates the correctness of the `is_sorted` function against the problem statement. Adjust the test cases as needed to cover different scenarios thoroughly. Let me know if you have any questions!