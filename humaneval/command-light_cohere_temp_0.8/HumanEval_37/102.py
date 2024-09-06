```python
def sort_even(lst):
    # Sort the list based on even index values
    lst[:] = sorted(lst, key=lambda x: x[1])
    return lst

# Test cases
test_sort_even = []
test_cases = [
    [ [1, 2, 3], [5, 6, 3, 4], [2, 8, 1, 10], [3, 6, 5, 4] ],
    [0, 7, 4, 5, 6, 3]
]

for case in test_cases:
    test_sort_even.append(list(case))
    assert sorted(test_sort_even) == case
```