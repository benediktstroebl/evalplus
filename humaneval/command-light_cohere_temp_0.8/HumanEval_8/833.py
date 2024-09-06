```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3, 4], 10, 24,
    [10], 40, 1,
    [5, 6, 7], 180, 28,
]

for case in test_cases:
    print(sum_product(case))
```
This code defines a Python function called sum_product, which takes a list of integers as input and returns a tuple of their sum and product. It uses a value of 1 for the product and initializes the sum variable to 0. The function then loops through each element in the list and updates the sum and product accordingly. Finally, it returns the product and sum.

The code then provides a list of test cases, and a for loop to iterate over each test case. It prints the test the output of the sum_product function for each test case.