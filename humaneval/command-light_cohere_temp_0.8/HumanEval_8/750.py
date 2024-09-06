```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
#Add test cases
test_cases = [
    [], 0]
  , [1, 2, 3], (10, 24)
  , [10, 20, 30], (300, 300)
]

for test_case in test_cases:
  print(sum_product(test_case))
``` 
This code defines a function `sum_product` which calculates the sum and product of a list of integers. It does this using a simple for-loop and product- Accumulation  It also has a series of test cases that pass the `sum_product` function with different list inputs.