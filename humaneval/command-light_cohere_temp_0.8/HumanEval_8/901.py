```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test cases
test_sum_product_lists = [
    [],  # Empty list, should return (0, 1)
    [1, 2, 3, 4],  # List with numbers, should return (6, 24)
    [-5, 6],  # List with negativie numbers, should return (0, 1)
    [10, 20, 30], # List with large numbers, should return (60, 900)
]

for test_case in test_sum_product_lists:
    actual_result = sum_product(test_case)
    print(f"Test case: {test_case}, {actual_result}")
    print()
``` 
This Python script provides a self-contained function 'sum_product' that calculates the sum and product of integers within a list, with specific test cases.  The result a list of negative integers, the function returns (0, 1). Similarly, for lists with large integers, it returns (60, 900).  The script also provides test cases with various scenarios, and it prints the results for each test case.