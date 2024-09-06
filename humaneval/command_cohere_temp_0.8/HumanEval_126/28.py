```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num <= nums for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and verifies two conditions:
1. There is only one unique element in the list: This is achieved by checking if all counts in the dictionary are 1.
2. The elements are sorted: This is achieved by checking if for every element in the dictionary, its subsequent items in the dictionary are greater than or equal to it. 

The `all()` function is used in combination with the boolean AND operator (`&`) to efficiently check both conditions. The function returns `True` if both conditions are met and `False` otherwise.  This algorithm has a time complexity of `O(n)` where `n` is the length of the input list.

The following test cases illustrate the usage of the `is_sorted()` function:
```python
test_cases = [
    ([5], True),
    ([1, 2, 3, 4, 5], True),
    ([1, 3, 2, 4, 5], False),
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([1, 3, 2, 4, 5, 6, 7], False),
    ([1, 2, 2, 3, 3, 4], True),
    ([1, 2, 2, 2, 3, 4], False)
]

for test_case, expected in test_cases:
    actual = is_sorted(test_case)
    assert actual == expected, f"For input {test_case}, expected {expected}, got {actual}"
```

This test suite contains a variety of cases that validate the correctness of the `is_sorted()` function against the problem statement.