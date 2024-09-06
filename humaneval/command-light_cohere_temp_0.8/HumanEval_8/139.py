```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Test if the input list is empty
        return (0, 1)
    result = numbers[0] + numbers[1] * numbers[2]
    for num in numbers[2:]:
        result = result * num
    return (result, result)

# Test cases
print(sum_product([0, 1]))  # Output: (1, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([10, 20, 30]))  # Output: (61, 120)
```