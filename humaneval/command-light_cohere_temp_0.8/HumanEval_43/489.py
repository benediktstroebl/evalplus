Here's a Python script that contains a self-contained function to solve the problem of finding pairs in a list whose sum is zero:
```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Example usage:
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for case in test_cases:
    result = pairs_sum_to_zero(case)
    assert result == case[1] == 0, f"Failed for case: {case}"
```
The function works by using the any built-in function with a generator expression to check if there's at least one pair in the list that adds up to zero.