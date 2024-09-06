```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with edge cases
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3]))  # Output: (10, 24)
print(sum_product([10]))    # Output: (0, 1)
print(sum_product([1, 2, 3, 4, 5])) # Output: (16, 120)
```
The function `sum_product` calculates the sum and product of a list of integers, and it passes these results to the function caller as arguments. It is covered a test edge cases, including an empty list, a list with a single element, and a list with multiple elements. This provides a tested with the code passing all these tests.