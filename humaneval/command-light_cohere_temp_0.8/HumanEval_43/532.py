```python
def pairs_sum_to_zero(lst):
    s = 0
    for i, num in enumerate(lst):
        if sum(num) == 0:
            s += 1
    return s == len(lst)

# Test
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test in test_cases:
    result = pairs_sum_to_zero(test)
    assert result == test[0], f"Test {test} failed: {result}"
```
The function checks if there are two elements in the list that sum up to zero. The function then returns "True" if this condition is met and "False" otherwise.