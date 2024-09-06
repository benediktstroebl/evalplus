```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of a list of integers.
    Args:
    numbers: list of integers
    
    Returns: 
    - tuple (sum of all integers, product of all integers) 
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_data1 = [1, 2, 3]
test_data2 = [10, 20, 30]
test_data3 = []
test_cases = [test_data1, test_data2, test_data3]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    expected_sum, expected_product = (sum(test_case) * product, product)
    assert actual_sum == expected_sum, f"Incorrect sum: {actual_sum}, expected: {expected_sum}"
    assert actual_product == expected_product, f"Incorrect product: {actual_product}, expected: {expected_product}"

```
This Python code defines a function `sum_product` that computes the sum and product of a list of integers. The function is designed with type hints to indicate the expected input and return types. 

Test cases are defined to verify the correctness of the function. The test cases include lists of integers, empty lists, and various combinations of integers, and the function's behavior is validated against these test cases.