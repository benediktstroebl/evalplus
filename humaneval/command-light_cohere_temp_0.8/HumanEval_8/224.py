```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of all integers in the list.
    Args: 
        - numbers: list of integers
    Returns: 
        - sum: sum of all integers in numbers 
        - product: product of all integers in numbers
    """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Test cases
test_cases = [
    [], (0, 1) 
   ":[1, 2, 3, 4], (10, 24)
    [5, 6, 7], (30, 120)
    [10, 20, 30], (250, 3000)
]

for test_num, test_expect in test_cases:
    actual_result = sum_product(test_num)
    print(f"Expected: {test_expect}, Actual: {actual_result}")
```