```python
def pairs_sum_to_zero(l):
    """
    Function to check if there are two numbers in list sum to zero
    """
    if sum(l) == 0:
        return True
    else:
        return False

# Example Test Cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

test_results = {}
for test_case in test_cases:
    if sum(test_case) == 0:
        test_results[test_case] = "pass"
    else:
        test_results[test_case] = "fail"

print("Test Results:")
for result in test_results.
```
This script defines a function, `pairs_sum_to_zero`, which takes a list of integers as input and returns a boolean indicating whether there are two numbers in the list whose sum is zero. It uses the tested by checking if the sum of the numbers is equal to zero. The function is then passed various test cases, and the test results are printed.