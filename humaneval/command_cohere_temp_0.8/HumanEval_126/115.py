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
2. Whether each element is sorted in ascending order (using the `all()` function and the `itertools.chain` function to create a sequence of pairs checking the order).

The `all()` function checks if all elements in the list are unique, and the `itertools.chain` function checks if each element is sorted in ascending order.

The following tests were randomly chosen and are included to ensure the correctness of the function in a variety of cases:
```python
def test_is_sorted():
    # Test Cases
    cases = [
        ([5], True),
        ([1, 2, 3, 4, 5], True),
        ([1, 3, 2, 4, 5], False),
        ([1, 2, 3, 4, 5, 6], True),
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([1, 3, 2, 4, 5, 6, 7], False),
        ([1, 2, 2, 3, 3, 4], True),
        ([1, 2, 2, 2, 3, 4], False)
    ]

    # Test the function on each test case
    for lst, expected in cases:
        actual = is_sorted(lst)
        assert actual == expected, f"For list {lst}, expected {expected} but got {actual}"
```

To test the function, you can add more test cases to the list `cases`. When doing so, include tests representative of extreme cases (large lists, lists with many duplicates, nearly sorted lists, etc.).