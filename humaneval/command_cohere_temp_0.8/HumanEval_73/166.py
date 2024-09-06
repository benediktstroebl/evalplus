```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. The function uses a `for` loop to iterate over each pair of corresponding elements in the input array and its reverse. If the elements don't match, a count is incremented. Finally, the count of mismatches is returned, which represents the smallest number of changes needed to make the array palindromic.

This approach has a time complexity of O(n^2) due to the pairwise comparisons between elements in the input array and its reverse. It is not the most efficient approach but fulfills the requirement of the given problem statement. 

The function can be tested as follows:
```python
test_cases = [
    ([1, 2, 3, 5, 4, 7, 9, 6], 4),
    ([1, 2, 3, 4, 3, 2, 2], 1),
    ([1, 2, 3, 2, 1], 0),
]

for expected, arr in test_cases:
    assert smallest_change(arr) == expected
```

This block of code helps verify the correctness of the `smallest_change` function against predefined test cases.