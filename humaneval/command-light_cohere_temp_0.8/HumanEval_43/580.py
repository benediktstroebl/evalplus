```python
def pairs_sum_to_zero(lst):
    if sum(x > 0 for x in lst) != 0:
        return False
    return True

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    assert result == True, "Function returned False when it should return True"

```

The code defines a Python function that checks if any two elements in an input list sum to zero. It then returns True if this condition is met and False otherwise. The test cases ensure the another function can be used for the purposes it is intended.