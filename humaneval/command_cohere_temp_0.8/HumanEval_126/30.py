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

The function utilizes a dictionary (`dups`) to track the occurrence of each unique number in the list. It first checks if each number in the list occurs only once in an efficient `any()` checker. Then, it verifies that the number occurring in the list is less than the next number in a tuple `(num, nums)` for each number tracked in the `dups` dictionary. This checks the list's ascending order and whether there's only one occurrence of each number. 

The following tests reflect the example use cases provided above:
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
    assert is_sorted(test_case) == expected
```