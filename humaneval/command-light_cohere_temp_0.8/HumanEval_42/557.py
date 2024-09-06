```python
def incr_list(lst):
    lst[0] += 1
    lst[-1] += 1  # We are considering 1 and last elements as base case
    for i in range(1, len(lst)):
        lst[i] += lst[i - 1]
    return lst

# Test cases
test_incr_list = [
    [(1, 2), (3, 4), (5, 6), (2, 3), (3, 4)],
    (5, 3, 5, 2, 3, 3, 9, 0, 123),
    ([6, 4, 6, 3, 4], [10, 1, 124])
]

# Function call and tests results
test_incr_list = incr_list(test_incr_list)
for case, expected in test_incr_list:
    assert list(case) == expected, "Incorrect result for case: " + "
```
Do feel free to adapt and use this script to test your function.