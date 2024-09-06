```python
def max_element(lst):
    if not_positive(lst) and not_divisible(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

def not_divisible(lst):
    return all(x % 1 == 0 for x in lst)

# Test cases
positive_test_cases = [5, 0, 123, [-5], [2, 3])
divisible_test_cases = [2, 3, [1, 2, 3], [1, 2, 3, 4])

for test_case in positive_test_cases:
    actual_result = max_element(test_case)
    assert actual_result > 0, f"Got negative result for positive list: {test_case}"

for test_case in divisible_test_cases:
    actual_result = max_element(test_case)
    assert actual_result % 1 == 0, f"Got non-integer result for divisible list: {test_case}"
```
This code defines a function `max_element` that returns the maximum element in a list. The `not_positive` and `not_divisible` helper functions ensure the input list is valid for the operation. The code also provides test cases to validate the correctness of the `max_element` function.