```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
test_numbers = [1, 2, 3, 4]
result = sum_product(test_numbers)
print(result)  # Output: (6, 24)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function iterates through numbers in the list and accumulates the sum and product values. It then returns a test the function by providing a list of numbers [1, 2, 3, 4] as an argument and prints the result, which should be the sum and product of these numbers. The output should be (6, 24).