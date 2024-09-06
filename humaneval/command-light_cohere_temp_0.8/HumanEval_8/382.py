```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
sum_product_test_cases = [
    [], (0, 1),
    [1, 2, 3], (6, 6),
    [1, 2, 3, 4], (10, 24)
]

for test_case in sum_product_test_cases:
    actual_result = sum_product(test_case)
    expected_result = next(expected_ for expected_, _ in zip(*sum_product_test_cases))
    print(f"Test case: {test_case}, {actual_result}, {expected_result}")
    assert actual_result == expected_result
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function first checks if the list is empty and returns 0 and 1 in that case. Additionally, it returns the expected result by applying the sum and product functions to the list of integers.

The code also provides a list of test cases, and then it iterates over each test case. It computes the latter by calling the `sum_product` function with the corresponding input. The actual result is stored in the `actual_result` variable. It compares this to the expected result retrieved from the corresponding test case in the `sum_product_test_cases` list. Finally, it asserts that the actual result matches the expected result using the `assert` statement with the `assertEqual` function.