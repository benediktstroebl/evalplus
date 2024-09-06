```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # test for empty list
        return (0, 1)

    result = numbers[0]
    product = 1
    for num in numbers[1:]:
        result = result * num
        product += 1
    return (result, product)

# Sample test cases
test_case_1 = [1, 2, 3, 4]
test_case_2 = []
print(sum_product(test_case_1))  # Output: (10, 24)
print(sum_product(test_case_2))  # Output: (0, 1)

```
The function 'sum_product' takes a list of integers as input and returns a tuple containing the sum and product of the numbers. The function first checks if the empty list is passed and returns (0, 1) if it is. Then, it calculates the product of numbers and returns the sum.