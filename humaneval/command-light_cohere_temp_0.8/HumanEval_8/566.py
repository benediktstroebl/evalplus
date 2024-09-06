```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases for the function
test_sum_product = [
    [[]],
    [1, 2, 3],
    [10, 20, 30],
]

for test_case in test_sum_product:
    actual_result = sum_product(test_case)
    expected_result = next(test_sum_product)
    print(f"Test case {test_case}:\nactual_result={actual_result}, expected_result={expected_result})
```
This code defines a function sum_product that calculates the sum and product of a list of integers. The function first checks if the list is empty, returning 0 and 1 in such case. Then, it uses the product function to calculate the product of the integers in the list and sum function to calculate the sum. The function returns a result, which is a tuple of the sum and product values. Finally, the code provides a list of test cases to verify the correctness of the sum_product function.