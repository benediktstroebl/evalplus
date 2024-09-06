```python
def pairs_sum_to_zero(lst):
    if sum(lst) == 0:
        return "The list has two distinct elements sumiding to zero."
    else:
        return "The list does not have two distinct elements sumiding to zero."

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_case in test_cases:
    print(f"Testing case: {test_case}")
    actual_result = pairs_sum_to_zero(test_case)
    expected_result = "The list has two distinct elements sumiding to zero"
    print(f"Actual result: {actual_result}, f"Expected result: {expected_result} ({test_case})")
    if actual_result != expected_result:
        print("Test failed")
    else:
        print("Test passed")
```
This code defines a function `pairs_sum_to_zero` that checks whether a list contains two numbers that sum to zero. The test cases are provided, and the function is then tested against them to ensure it works correctly.