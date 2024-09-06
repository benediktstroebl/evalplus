```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1
test_case1 = [1, 2, 3, 4]
result1 = sum_product(test_case1)
print("Test case 1 result:", result1)

# Test case 2 (empty list)
test_case2 = []
result2 = sum_product(test_case2)
print("Test case 2 result:", result2)

# Test case 3
test_case3 = [5, 6, 7]
result3 = sum_product(test_case3)
print("Test case 3 result:", result3)
``` 
This Python code defines a function called sum_product that calculates the sum and product of a list of integers. The function utilizes a `typing` module to ensure type hints and returns a tuple with the sum and product values. It then passes three test cases: an empty list, a list of integers, and a list of odd numbers, to demonstrate its functionality. The output will display the values of the results for each test case.