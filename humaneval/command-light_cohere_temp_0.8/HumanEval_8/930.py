```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3], (6, 6)
  ]

for test_case in test_cases:
    print(sum_product(test_case))
``` 
This script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The script then includes several test cases to verify the correctness of the sum_product function.