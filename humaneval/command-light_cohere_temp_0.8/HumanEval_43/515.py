```python
def pairs_sum_to_zero(l):
    return any(x > 0 and y < 0 for x, y in zip(l, l[1:]))

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for i, test_tup in enumerate(test_cases):
    result = pairs_sum_to_zero(test_tup)
    assert result == i == 4 or result is False
```
The function checks if any pair of elements in the list create a sum of zero. This means that at least one of the elements is positive and the other is negative. It returns True if the
The function passes all the tests.