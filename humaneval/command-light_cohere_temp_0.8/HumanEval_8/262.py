```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args:
    numbers: A list of integers
    
    Returns:
    A tuple of sum(numbers) and product(numbers)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#unit tests
test_sum_product = [
    [
        ((), (0, 1)),
        ([], (0, 1)),
        ([1, 2, 3, 4], (10, 24)),
        ([10, 20, 30], (50, 600)),
    ]
]

for case, expect in test_sum_product:
    actual = sum_product(case)
    print(f'Case: {case}, {actual}, {expect}')
```

The above Python script defines a function `sum_product` that calculates the sum and product of a given list of integers, and passes these calculations along with the corresponding tests.  It utilizes the _ typing module to ensure type-safety and provide more readable code, which is beneficial for better code organization and maintainability.