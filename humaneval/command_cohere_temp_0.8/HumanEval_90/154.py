```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    elif lst[-2] > lst[-1]:
        return lst[-2]
    else:
        return lst[-1]
```

The function `next_smallest()` employs list comprehension to examine the second last and last elements of the list `(lst[-2] and lst[-1])`. When the list has less than two elements (`len(lst) < 2`), the function returns `None`. When the second last element is greater than the last element, the function returns the second smallest as the second last element `(lst[-2])`. Otherwise, the function returns the second smallest as the last element of the list `(lst[-1])`.

Here is a simple test suite to ensure correctness:
```python
TEST_CASES = [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([], None),
    ([1, 1], None),
    ([1, 2, 3, 4, 5, 6], 3),
    ([2, 3, 4, 5, 1], 1),
]

for test_case, expected in TEST_CASES:
    actual = next_smallest(test_case)
    assert actual == expected, f"For list {test_case}, expected {expected}, got {actual}"
```