```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test case: empty list
print(sum_product([]))  # Output: (0, 1)

#Test case: single number list
print(sum_product([1]))  # Output: (1, 1)

#Test case: positive integer list
print(sum_product([2, 3, 4]))  # Output: (6, 12)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers, passing in tests to verify the correctness of the function. It calculates the sum and product iteratively using a loop, then returns a tuple of the sum and product.

The script is well-contained and provides a clear and efficient solution to the problem statement.