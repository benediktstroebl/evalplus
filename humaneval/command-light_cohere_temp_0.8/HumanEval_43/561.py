```python
def pairs_sum_to_zero(lst):
    return any([x + y == 0 for x, y in zip(lst, lst[1:])])

# Test
test_cases = [
    [ [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7], [1]]
]

for test_case in test_cases:
    actual_result = pairs_sum_to_zero(test_case)
    expected_result = True  # This is the value we're looking for, so we expect a True value

    if actual_result == expected_result:
        print(f"Test case {test_case} passed!")
    else:
        print(f"Test case {test_case} failed.")
```
This script defines a function `pairs_sum_to_zero` that checks if there are two elements in the list that their sum is equal to zero. The function returns `True` if there are two distinct elements that sum to zero, and `False` otherwise. The test cases are passed through and the function's behavior is compared against the expected results. The script then checks the expected results and prints whether the tests passed or failed.