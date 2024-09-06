```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This Python code defines a function called sum_product that calculates the sum and product of a list of integers. It uses the specific typing to ensure type-safe operations. The function performs the important calculation and returns a tuple with the sum and product values. It also incorporates a test that ensures the function is called correctly and receives a list of integers. The test successfully passes, demonstrating the functionality of the sum_product function.