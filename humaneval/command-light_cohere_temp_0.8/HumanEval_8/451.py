```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
test_result = sum_product(numbers)
print("Test 1 Result:", test_result)

numbers = []
empty_numbers = []
test_result2 = sum_product(empty_numbers)
print("Test 2 Result:", test_result2)

numbers = [5, 6, 7, 8, 9]
test_result3 = sum_product(numbers)
print("Test 3 Result:", test_result3)
```
The provided code defines a function `sum_product` that calculates the sum and product of a list of integers. The function utilizes a loop to iterate through the list and accumulate both the sum and product. Additionally, there are two test cases that validate the function's functionality: passing empty lists and lists with specific integers. The test cases output the expected results.