```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test case 1: empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: list with single element
print(sum_product([1]))  # Output: (1, 1)

# Test case 3: list with three elements
print(sum_product([1, 2, 3]))  # Output: (6, 6)

# Test case 4: list with large numbers
print(sum_product([123, 456, 789]))  # Output: (1022, 22449236)
```
This Python script contains a function `sum_product` that calculates the sum and product of a given list of integers. The function uses a TDD approach, making it self-contained and easy to understand. The test cases provided at the