```python
def pairs_sum_to_zero(lst):
    if sum(lst) == 0:
        return "Yes"
    else:
        return "No"

# Tests
test_pairs_sum_to_zero = [
    [
        [1, 3, 5, 0],
        [1, 3, -2, 1],
        [1, 2, 3, 7],
        [2, 4, -5, 3, 5, 7],
    ]

for test_case in test_pairs_sum_to_zero:
    actual_result = pairs_sum_to_zero(test_case)
    print(f"Test case {test_case}: {actual_result}")
```